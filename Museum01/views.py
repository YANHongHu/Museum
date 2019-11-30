import hashlib
import json
import random
import string

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from Museum01 import models


# 登录函数
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 获取用户名和密码
        name = request.POST.get('user_name')
        password = request.POST.get('password')
        # 尝试在用户表中查找此用户,若不存在则返回错误信息
        user = models.User.objects.get(user_name=name)
        if user:
            # 存在则进行密码匹配，取出随机字符串
            s = models.UserStr.objects.filter(user_name=name)[0].str
            # 创建MD5对象
            m = hashlib.md5()
            new_password = s + password + s
            b = new_password.encode(encoding='utf-8')
            m.update(b)
            new_password_md5 = m.hexdigest()
            # 如果密码正确进行身份判断，错误则返回错误信息
            if new_password_md5 == user.password:
                if user.authority == "root":
                    request.session['user_name'] = name
                    return render(request, 'home.html')
                else:
                    request.session['user_name'] = name
                    return render(request, 'home_root.html')
            else:
                pass
        else:
            return render(request, 'login.html', {'message': '此用户不存在'})

# 用户注册
def add_users(request):
    response = {}
    if request.method == "POST":
        # 获取用户名和密码
        body = json.loads(request.body)
        user_name = body['user_name']
        password = body['password']
        telephone = body['telephone']
        # 随机生成一个字符串
        s = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        # 生成一个md5对象
        m = hashlib.md5()
        # 用字符串对密码进行重新编码
        new_password = s+password+s
        # 将str编码至bytes
        b = new_password.encode(encoding='utf-8')
        m.update(b)
        new_password_md5 = m.hexdigest()
        # 在数据库中保存用户名和它对应的随机字符串
        try:
            models.UserStr.objects.create(user_name=user_name, str=s)
            # 保存经过随机字符串和MD5加密后的密码
            models.User.objects.create(user_name=user_name, password=new_password_md5, telephone=telephone)
        except Exception:
            response['status'] = False
            return JsonResponse(data=response, safe=False)
        else:
            response['status'] = True
            return JsonResponse(data=response, safe=False)
