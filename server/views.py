from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from server.models import Users


def user_login(request):
    stu_id = request.GET.get("stu_id")
    password = request.GET.get("password")
    user = authenticate(request, username=stu_id, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Login Success !" + user)
    else:
        return HttpResponse("Login Failed !")


def user_logout(request):
    logout(request)
    return HttpResponse("Logout Success !")


def user_register(request):
    stu_id = request.GET.get("stu_id")
    password = request.GET.get("password")
    user = Users.objects.create_user(stu_id=stu_id, password=password)
    user.save()
    return HttpResponse("Register Success !")


def user_change_info(request):
    pass


def activity_add(request):
    pass


def activity_part(request):
    pass


def activity_query(request):
    pass


def activity_list(request):
    pass


