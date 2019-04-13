#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from website import views

app_name = "website"
urlpatterns = [
    path('', views.index),
    path('<cate>', views.index, name="首页"),
    path('create/', views.create, name="添加网址"),
    path('search/', views.WebsiteSearch(), name="搜索")
]
