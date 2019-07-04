#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 21:45
# @Author  : icon
# @File    : urls.py
from class_dev.flask03.app import app
from class_dev.flask03 import views


app.add_url_rule('/case', view_func=views.cases)
app.add_url_rule('/', view_func=views.index)
