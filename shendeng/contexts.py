#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shendeng import settings


def lang(request):
    range10 = (x for x in range(10))
    return {'lang': settings.LANGUAGE_CODE, 'range10': range10}
