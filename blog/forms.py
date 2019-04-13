#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from blog.models import Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget
import os
from shendeng import settings


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'tags', 'belong']
        widgets = {'content': CKEditorUploadingWidget(attrs={'class': 'form-control'}),
                   'belong': forms.TextInput(attrs={'type': 'hidden'})}

    def clean_title(self):
        ret = super().clean()
        title = ret.get('title')
        return title

    def clean_content(self):
        ret = super().clean()
        content = ret.get('content')
        title = ret.get('title')
        content_path = BlogForm.write_blog_content(content, title)
        return content_path

    @staticmethod
    def write_blog_content(content, name):
        '''
        把博客内容写入文件
        '''
        base_path = os.path.join(settings.BASE_DIR, 'blog_files')   # 用os的作用是因为不同操作系统的文件路径格式不同。
        file_path = os.path.join(base_path, name + '.html')
        filecontent = str(content)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(filecontent)
        return file_path
