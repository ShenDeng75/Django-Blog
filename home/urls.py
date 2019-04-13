#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path
from home import views


app_name = "home"
urlpatterns = [
    path('', views.index, name="首页")
]
