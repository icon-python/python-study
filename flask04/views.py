#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 21:45
# @Author  : icon
# @File    : views.py
from test.flask04.app import app


@app.route('/')
def index():
    return 'index'


@app.route('/getonepro/<id>')
def get_project(id):
    try:
        id = int(id)
        if id in range(1, 5):
            pro = app.config['all'][id-1]
            return f'当前项目：{pro}'
        else:
            return '不存在该项目'
    except:
        return 'id只能为数字'


@app.route('/getallpro')
def get_all_projects():
    if not app.config['all'].__len__():
        app.config['all'] = '当前没有项目'
    content = '所有项目：{}'.format(str(app.config['all'])[1:-1])
    return content
