#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from blog import views

app_name = "blog"
urlpatterns = [
    path('', views.index, name="首页"),
    path('create_blog', views.create_blog, name="添加博客"),
    path('detail/<pk>/<slug>', views.detail, name="查看博客"),
    path('category/<tag>', views.category, name="博客分类"),
]

