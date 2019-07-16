#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 20:35
# @Author  : icon
# @File    : app.py


from flask import Flask, render_template, request, abort, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    phone = request.args.get('phone')
    response = Response(render_template('register.html', msg="手机号不能为空"), status=400,
                        content_type="text/html;charset=utf-8")
    if not phone:
        # abort(response)
        return render_template('register.html', msg="手机号不能为空"), 400, {"content_type": "text/html;charset=utf-8"}


if __name__ == '__main__':
    app.run(debug=True)
