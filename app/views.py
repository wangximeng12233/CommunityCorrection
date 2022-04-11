import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
#首页
from app import models


def index(request):
    if request.method == "POST":
        pass
    else:
        result = {}
        username = request.COOKIES["username"]
        user = models.User.objects.get(username=username)
        role = user.auth
        result["role"] = role
        visit = models.Visit.objects.get(id=1)
        visitCount = str(int(visit.count)+1)
        visit.count = visitCount
        visit.save()
        result["visit"] = visitCount
        result["fxcount"] = len(models.User.objects.filter(auth="服刑人员"))
        result["xlcount"] = len(models.User.objects.filter(auth="心理咨询师"))
        result["glcount"] = len(models.User.objects.filter(auth="管理员"))
        resp = render(request, "index.html",result)
        return resp

#登录
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        data = models.User.objects.filter(username=username)
        if len(data) == 1:
            if data[0].password == password:
                resp = JsonResponse({"flag": True})
                resp.set_cookie("username", username)
                return resp
            else:return JsonResponse({"flag": False})
        else:return JsonResponse({"flag": False})

    else:
        resp = render(request, "login.html")
        resp.delete_cookie("username")
        return resp

def reg(request):
    if request.method == "POST":
        try:
            username = request.POST.get("username","")
            password = request.POST.get("password", "")
            phone = request.POST.get("phone", "")
            true_name = request.POST.get("true_name", "")
            sex = request.POST.get("sex", "")
            role = request.POST.get("role", "")
            models.User.objects.create(
                username=username,
                password=password,
                phone=phone,
                trueName=true_name,
                sex=sex,
                auth=role
            )
            return JsonResponse({"flag":True})
        except:return JsonResponse({"flag":False})

#个人信息
def information(request):
    username = request.COOKIES["username"]
    user = models.User.objects.get(username=username)
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            phone = request.POST.get("phone")
            trueName = request.POST.get("trueName")
            sex = request.POST.get("sex")
            file = request.FILES.get("headpic")
            position = request.POST.get("position")
            if file != None:
                file_path = "./static/img/" + str(uuid.uuid4()) + '.jpg'
                with open(file_path, 'wb') as f:
                    for chunk in file.chunks():
                        f.write(chunk)
                user.headpic = file_path[1:]
            user.username = username
            user.phone = phone
            user.trueName = trueName
            user.sex = sex
            user.position = position
            user.save()
            resp = JsonResponse({"flag": True})
            resp.set_cookie("username", username)
            return resp
        except Exception as e:
            print(e)
            return JsonResponse({"flag": False})
    else:
        result = {}
        user = models.User.objects.get(username=username)
        role = user.auth
        result["role"] = role
        result["user"] = user
        resp = render(request, "information.html", result)
        return resp