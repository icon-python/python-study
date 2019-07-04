#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 20:19
# @Author  : icon
# @File    : app.py
# import uuid

from flask import Flask, request, redirect

# print(uuid.uuid4())
app = Flask(__name__)
from class_dev.flask03.urls import *  # 防止互相导入时产生问题，需要用时，只引用对方的代码，不运行引用导入代码

# print(app.url_map)


# @app.route('/cases/<int:id>')  # float string path(可包含斜杠/)
# def get_case(id):
#     id = request.args.get('id')
#     return f'{id}'
#     return f'{id}'
# @app.route('/')
# def index():
#     return 'index'


# @app.route('/cases/', methods=['POST', 'GET'], endpoint='cases', redirect_to='/', defaults={'id':3})
# @app.route('/cases/', methods=['POST', 'GET'], endpoint='cases', defaults={'id':3}) #  endpoint视图函数别名
# def get_case(id):
#     print(id)
#     # return redirect('/')
#     return 'hello'
# 默认参数：1.defaults={'id':3}；2.视图函数中id=3 id=None
#  集中注册适合大型项目，可以新建url.py管理
# app.add_url_rule('/case', view_func=get_case)
# print(app.url_map)  # url和视图函数绑定关系
# 重定向  1.@app.route(redirect_to='/');  2.redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
