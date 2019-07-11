#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author:muji
# datetime:2019/7/11 19:58
# 技术债
# 搜索引擎。

# 不停的学习，和周边的同事，
#

from flask import Flask, request, redirect, url_for, render_template, abort, make_response, jsonify
from werkzeug.routing import Rule

app = Flask(__name__, static_url_path='/src')


# URL 和 视图函数： 绑定关系==》 endpoint 端点
# 全局错误处理
@app.errorhandler(500)
def server_error(error):
    return render_template('error_500.html')


@app.errorhandler(404)
def server_error(error):
    return render_template('user_error_401.html')


# app.register_error_handler(500, server_error)

class UserError(Exception):
    pass


@app.errorhandler(UserError)
def server_error(error):
    # return render_template('user_error_401.html', error=error), 401
    res = jsonify({'msg':'401'})
    res.status = '401'
    return res


# namedtuple class

@app.route('/')
# /login, def login
def index():
    # try:
    if not request.args.get('username'):
        raise UserError('user error')
    return render_template('index.html')


# 项目列表?project_id=3


@app.route('/login', endpoint='login')
# /login, def login
def login():
    return 'login'


if __name__ == '__main__':
    app.run(debug=True)
