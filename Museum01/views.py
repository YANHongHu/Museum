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
        user = models.User.objects.filter(telephone=telephone).first()
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
                        root = {}
                        root['user_name'] = user.user_name
                        root['head_img'] = user.head_img
                        return render(request, 'home_root.html', {'root': root})
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
            new_password = s + password + s
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


def first_qin(request):
    cloths = []
    if request.method == 'GET':
        costumes = models.Costume.objects.filter(dynasty__in=["夏", "商", "周", "春秋战国"])
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
        else:
            return render(request, "firstqin.html", {"cloths": cloths})


def qing_han(request):
    cloths = []
    if request.method == 'GET':
        costumes = models.Costume.objects.filter(dynasty__in=["秦", "西汉", "东汉"])
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
            return render(request, "qinghan.html", {'cloths': cloths})
        else:
            return render(request, "qinghan.html", {'cloths': cloths})


def sui_tang(request):
    cloths = []
    if request.method == 'GET':
        costumes = models.Costume.objects.filter(dynasty__in=["隋", "唐"])
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
            return render(request, "sui_tang.html", {"cloths": cloths})
        else:
            return render(request, "sui_tang.html", {"cloths": cloths})


def two_song(request):
    cloths = []
    if request.method == 'GET':
        costumes = models.Costume.objects.filter(dynasty__in=["南宋", "北宋"])
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
            return render(request, "two_song.html", {'cloths': cloths})
        else:
            return render(request, "two_song.html", {'cloths': cloths})


def y_m_q(request):
    cloths = []
    if request.method == 'GET':
        costumes = models.Costume.objects.filter(dynasty__in=["元", "明", "清"])
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
            return render(request, "y_m_q.html", {"cloths": cloths})
        else:
            return render(request, "y_m_q.html", {"cloths": cloths})


def search(request):
    cloths = []
    if request.method == "POST":
        cs_name = request.POST["cs_name"]
        print(cs_name)
        costumes = models.Costume.objects.filter(cs_name__contains=cs_name)
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
            return render(request, "search.html", {"cloths": cloths})
        else:
            return render(request, "search.html", {"cloths": cloths})


def single_cloth(request):
    if request.method == "GET":
        cs_name = request.GET.get("name")
        print(cs_name)
        costume = models.Costume.objects.filter(cs_name=cs_name)[0]
        print(costume)
        single = {}
        single['cs_name'] = cs_name
        single['describe'] = costume.describe
        single['material'] = costume.material
        single['texture'] = costume.texture
        url_image = []
        url_imgs = models.Image.objects.filter(costume_name=costume.cs_name)
        for url_img in url_imgs:
            url_image.append(url_img.url_img)
        single['url_images'] = url_image
        try:
            url_mp3 = models.MP3.objects.filter(costume_name=costume.cs_name)[0]
            url_mp4 = models.MP4.objects.filter(costume_name=costume.cs_name)[0]
            print(url_mp4.url_mP4)
            print(url_mp3.url_mp3)
            if url_mp3:
                single['url_mp3'] = url_mp3.url_mp3
            else:
                single['url_mp3'] = None
            if url_mp4:
                single['url_mp4'] = url_mp4.url_mP4
            else:
                single['url_mp4'] = None
        except:
            return render(request, "single.html", {"cloth": single})
        else:
            return render(request, "single.html", {"cloth": single})


def module(request):
    cloths = []
    if request.method == 'GET':
        costumes = models.Module.objects.filter()
        if costumes is not None:
            for costume in costumes:
                print(costume.md_name)
                single = {}
                single["cs_name"] = costume.md_name
                single["describe"] = costume.describe
                print(single)
                single["url_img"] = costume.url_img
                cloths.append(single)
            return render(request, "module.html", {"cloths": cloths})
        else:
            return render(request, "module.html", {"cloths": cloths})


def single_module(request):
    if request.method == "GET":
        md_name = request.GET.get("name")
        print(md_name)
        single = {}
        module = models.Module.objects.filter(md_name=md_name)[0]
        single["md_name"] = md_name
        single["url_md"] = module.url_md
        single["url_grain"] = module.url_grain
        return render(request, "0.加载obj文件.html", {"module": single})




def add_cloth(request):
    if request.method == "GET":
        return render(request, "add_cloth.html")


def add(request):
    pass