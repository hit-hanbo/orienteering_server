# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from server.models import Users, Activity
import json


# 用户登录调用函数
def user_login(request):
    msg = {
        "code": 0,
        "message": ""
    }
    stu_id = request.GET.get("stu_id")
    password = request.GET.get("password")
    user = authenticate(request, username=stu_id, password=password)
    if user is not None:
        login(request, user)
        msg["code"] = 1
        msg["message"] = "Login Success !"
    else:
        msg["code"] = 0
        msg["message"] = "Login Failed !"
    return HttpResponse(
        json.dumps(msg)
    )


# 用户注销调用函数
def user_logout(request):
    logout(request)
    msg = {
        "code": 1,
        "message": "Logged Out !"
    }
    return HttpResponse(
        json.dumps(msg)
    )


# 用户注册调用函数
def user_register(request):
    stu_id = request.GET.get("stu_id")
    password = request.GET.get("password")
    name = request.GET.get("name")
    user_info = request.GET.get("user_info")
    msg = {
        "code": 0,
        "message": ""
    }
    try:
        user = Users.objects.create_user(stu_id=stu_id, password=password)
    except:
        msg["code"] = 0
        msg["message"] = "Failed to register !"
        return HttpResponse(
            json.dumps(msg)
        )
    user.name = name
    user.user_info = user_info
    user.save()
    msg["code"] = 1
    msg["message"] = "Register Success !"
    return HttpResponse(
        json.dumps(msg)
    )


# 更改用户信息调用函数
def user_change_info(request):
    msg = {
        "code": 0,
        "message": ""
    }
    pass


# 查询用户信息调用函数
def user_query(request):
    stu_id = request.GET.get("stu_id")
    try:
        user = Users.objects.get(stu_id=stu_id)
    except:
        msg = {
            "code": 0,
            "message": "Failed to query !"
        }
        return HttpResponse(
            json.dumps(msg)
        )
    user_info = {
        "stu_id": user.user_info,
        "name": user.name,
        "user_info": user.user_info,
    }
    return HttpResponse(
        json.dumps(user_info)
    )


# 查询用户参加的活动调用函数
def user_activity_list(request):
    stu_id = request.GET.get("stu_id")
    user = Users.objects.get(stu_id=stu_id)
    activitys = user.activity_set.all()
    user_activitys = dict()
    for activity in activitys:
        user_activitys[activity.title] = activity.title
    return HttpResponse(
        json.dumps(user_activitys)
    )


# 添加新的活动调用函数
def activity_add(request):
    title = request.GET.get("title")
    datetime = request.GET.get("datetime")
    location = request.GET.get("location")
    info = request.GET.get("info")
    try:
        activity = Activity(title=title, datetime=datetime,
                        location=location, activity_info=info)
    except:
        msg = {
            "code": 0,
            "message": "Failed to add new activity !"
        }
        return HttpResponse(
            json.dumps(msg)
        )
    activity.save()
    msg = {
        "code": 1,
        "message": "Add new activity Success !"
    }
    return HttpResponse(
        json.dumps(msg)
    )


# 用户参与某个活动调用函数
def activity_part(request):
    stu_id = request.GET.get("stu_id")
    title = request.GET.get("title")
    user = Users.objects.get(stu_id=stu_id)
    activity = Activity.objects.get(title=title)
    activity.partners.add(user)
    msg = {
        "code": 1,
        "message": "Participate Success !"
    }
    return HttpResponse(
        json.dumps(msg)
    )


# 查询某个活动详细信息的函数
def activity_query(request):
    title = request.GET.get("title")
    activity = Activity.objects.get(title=title)
    partners = activity.partners.all()
    partners_stu_id = dict()
    for people in partners:
        partners_stu_id[people.stu_id] = people.stu_id
    query = {
        "title": activity.title,
        "datetime": activity.datetime,
        "location": activity.location,
        "info": activity.activity_info,
        "partners": partners_stu_id
    }
    return HttpResponse(
        json.dumps(query)
    )


# 查询当前可以参加的活动列表的函数
def activity_list(request):
    activities = Activity.objects.all()
    query_list = dict()
    for activity in activities:
        query_list[activity.title] = activity.title
    return HttpResponse(
        json.dumps(query_list)
    )


