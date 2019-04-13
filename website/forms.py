#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from website.models import Website


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['name', 'url', 'category', 'belong', 'describe']
        widgets = {
            'belong': forms.TextInput(attrs={'type': "hidden"})
        }

    def clean_url(self):
        url = self.cleaned_data['url']

        if Website.objects.filter(url=url).exists():
            raise forms.ValidationError("该URL已存在")
        return url
