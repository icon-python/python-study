#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 21:01
# @Author  : icon
# @File    : app.py


from flask import Flask, render_template, request, redirect, abort, url_for, jsonify, flash

app = Flask(__name__)
app.secret_key = 'flash secret_key'


class UserError(Exception):
    pass


# URL 和 视图函数： 绑定关系==》 endpoint 端点
# 全局错误处理
@app.errorhandler(UserError)
def server_error(error):
    print(error, type(error))  # error:<class '__main__.UserError'>
    return render_template('error_500.html')


@app.errorhandler(401)
def server_error(error):
    # return render_template('error_401.html')
    return jsonify({"msg": error.__dict__}), 201


@app.route('/')
def index():
    if not request.args.get('username'):
        # return redirect('/login')
        # abort(500)
        abort(401)
        # raise UserError("user error")
    return redirect(url_for('log'))


@app.route('/login', endpoint='log')
def login():
    return render_template('index.html')


@app.route('/projects')
def projects():
    projects = [
        {"name": "项目1", "interface_num": 23, "create_time": "2019/1"},
        {"name": "项目2", "interface_num": 24, "create_time": "2019/1"},
        {"name": "项目3", "interface_num": 25, "create_time": "2019/1"},
    ]
    flash("flash test")
    # return jsonify({"msg":[p for p in projects]})
    return render_template('index.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
