#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 11:44
# @Author  : icon
# @File    : method_view.py

import time
from flask import Flask
from flask.views import MethodView

app = Flask(__name__)


def log_time(f):
    def decorator(*args, **kw):
        st = time.time()
        res = f(*args, **kw)
        print(f'{time.time() - st}')
        return res
    return decorator


class MyMethodView(MethodView):
    methods = ["GET", "POST"]
    decorators = [log_time,]

    def get(self):
        return 'get'

    def post(self):
        return 'post'


f = MyMethodView.as_view('user')
app.add_url_rule('/project', view_func=f, methods=["GET", "POST", "PUT", "DELETE"])

if __name__ == '__main__':
    app.run(debug=True)
