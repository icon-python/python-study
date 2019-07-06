#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: icon
# datetime:2019/7/6 11:16


from flask import Flask, request, Request

app = Flask(__name__)
# Request()


@app.route('/', methods=['GET', 'POST'])
def index():
    a = request
    # get 请求 # request, 请求相关，flask,app, wsgi: 环境变量
    get_data = request.args
    form_data = request.form  # 表单
    json_data = request.json  # json # header {appliction/json}
    file_data = request.files  # file
    # AJAX, json, 请求投，XHR:
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
