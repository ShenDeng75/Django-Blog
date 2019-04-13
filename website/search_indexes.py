#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from haystack import indexes
from website.models import Website


class WebsiteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='belong')        # 这些字段可以用来在搜索结果中显示
    pub_date = indexes.CharField(model_attr='create_date')

    def get_model(self):
        return Website

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
