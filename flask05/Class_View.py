#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 10:32
# @Author  : icon
# @File    : Class_View.py
import time
from flask import Flask, request
from flask.views import View

app = Flask(__name__)


def log_time(f):
    def decorator(*args, **kw):
        st = time.time()
        res = f(*args, **kw)
        print(f'{time.time() - st}')
        return res
    return decorator


class ProjectView(View):
    methods = ["GET", "POST"]
    decorators = [log_time, ]

    def get(self):
        return 'get'

    def post(self):
        return 'post'

    def dispatch_request(self):  # 分配请求
        dispatch_pattern = {'GET': self.get, 'POST': self.post}
        return dispatch_pattern.get(request.method)()


f = (ProjectView.as_view('project'))
app.add_url_rule('/project', view_func=f)

if __name__ == '__main__':
    app.run(debug=True)
