#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 21:01
# @Author  : icon
# @File    : app.py
import json
from _datetime import datetime
import time

from flask import Flask, render_template, request, redirect, abort, url_for, jsonify, flash, session

app = Flask(__name__)
app.secret_key = '123456'


class UserError(Exception):
    pass


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


@app.route('/login/<username>', endpoint='log')
def login(username):
    session['user'] = username
    return render_template('index.html')


# @app.template_filter('s_time')
def strf_time(timestamp):
    return datetime.fromtimestamp(timestamp)
app.add_template_filter(strf_time,'s_time' )


@app.template_test()
def jsoned(my_str):
    try:
        json.loads(my_str)
        return True
    except:
        return False
# app.jinja_env.globals['jsoned'] =jsoned


@app.context_processor
def add_ctc():
    def get_now(timestamp):
        return datetime.fromtimestamp(timestamp)

    return {'get_n': get_now, 'temp_var': 20}


@app.route('/projects')
def projects():
    projects_all = [
        {"name": "projectone", "interface_num": 23, "create_time": int(time.time())},
        {"name": "projecttwo", "interface_num": 24, "create_time": int(time.time())},
        {"name": "projectthree", "interface_num": 25, "create_time": int(time.time())},
    ]
    flash("flash test")
    # return jsonify({"msg":[p for p in projects]})
    return render_template('index.html', projects=projects_all, msg=None, my_json='{"username":"admin"}')


if __name__ == '__main__':
    app.run(debug=True)
