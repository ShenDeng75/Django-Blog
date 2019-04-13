#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import Author
from django.shortcuts import get_object_or_404
import re


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Author
        fields = ['nick', 'tel']

    def clean_nick(self):
        nick = super().clean().get('nick')
        if str(nick).strip() == "":
            raise forms.ValidationError("昵称不能为空")
        author = get_object_or_404(Author, user=self.request.user)
        if Author.objects.filter(nick=nick).exists() and nick != author.nick:
            raise forms.ValidationError("该昵称太火了，换一个吧！")
        return nick

    def clean_tel(self):
        tel = super().clean().get('tel')
        if not re.match(r"^1[34578]\d{9}$", tel):
            raise forms.ValidationError("请输入有效的电话号码")
        return tel


# 注册后执行的表单验证
class SignupForm(forms.Form):
    def signup(self, request, user):
        user_profile = Author()
        user_profile.user = user
        user.save()
        user_profile.save()
