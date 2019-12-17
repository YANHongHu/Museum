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
    if request.method == 'POST': 
        # 获取用户名和密码
        telephone = request.POST.get('telephone')
        print(telephone)
        password = request.POST.get('password')
        print(password)
        # 尝试在用户表中查找此用户,若不存在则返回错误信息
        user = models.User.objects.filter(telephone=telephone)[0]
        print(user)
        if user:
            # 存在则进行密码匹配，取出随机字符串
            user_name = user.user_name
            s = models.UserStr.objects.filter(user_name=user_name)[0].str
            # 创建MD5对象
            m = hashlib.md5()
            new_password = s + password + s
            b = new_password.encode(encoding='utf-8')
            m.update(b)
            new_password_md5 = m.hexdigest()
            try:
                request.session['user_name'] = user_name
            except LookupError:
                pass
            else:
                # 如果密码正确进行身份判断，错误则返回错误信息
                if new_password_md5 == user.password:
                    if user.authority == "root":
                        print(user.authority == "root")
                        return render(request, 'home_root.html')
                    else:
                        return render(request, 'home.html')
                else:
                    return render(request, 'home.html', {'message': '用户名或密码错误'})
        else:
            return render(request, 'home.html', {'message': '此用户不存在,请您先注册'})
    elif request.method == 'GET':
        return render(request, 'home.html')


# 管理员注册
def register(request):
    if request.method == "POST":
        # 获取用户名和密码
        user_name = request.POST['user_name']
        password = request.POST['password']
        telephone = request.POST['telephone']
        print(password)
        obj = models.User.objects.filter(user_name=user_name, telephone=telephone)
        if obj:
            return render(request, 'home.html', {'message': '你已经注册过了'})
        else:
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
            models.UserStr.objects.create(user_name=user_name, str=s)
            # 保存经过随机字符串和MD5加密后的密码
            models.User.objects.create(user_name=user_name, password=new_password_md5, telephone=telephone)
            return render(request, 'home.html', {'message': '注册成功'})
    elif request.method == 'GET':
        return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')


def find_cloth(request):
    cloths = []
    if request.method == 'GET':
        costumes = models.Costume.objects.filter(dynasty="先秦")
        if costumes is not None:
            for costume in costumes:
                print(costume.cs_name)
                single = {}
                single["cs_name"] = costume.cs_name
                single["describe"] = costume.describe
                print(single)
                url_img = models.Image.objects.filter(costume_name=costume.cs_name)[0]
                single["url_img"] = url_img.url_img
                cloths.append(single)
            return render(request, "firstqin.html", {"cloths": cloths})


def search_cloth(request):
    pass