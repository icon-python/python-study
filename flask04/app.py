#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 20:19
# @Author  : icon
# @File    : app.py
# import uuid

from flask import Flask

app = Flask(__name__)
app.config['all'] = ['项目1', '项目2', '项目3', '项目4']
from test.flask04.views import *

if __name__ == '__main__':
    app.run(debug=True)
