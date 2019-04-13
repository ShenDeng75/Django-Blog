#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from author import views

app_name = "author"
urlpatterns = [
    path('profile/', views.profile, name="跳转"),
    path('profile/profile_update/', views.profile_update, name="修改信息"),
    path('profile/profile_detail/', views.profile_detail, name="显示个人信息"),
]