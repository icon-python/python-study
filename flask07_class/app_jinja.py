#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/7/11 15:59
import re
import time
from datetime import datetime
import json
from flask import Flask, abort, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOFOF'

# enumerate()

@app.route('/')
def index():
    projects = [
        {"name":"项目1", "interface_num": 23, "create_time":"2019/1"},
        {"name": "项目2", "interface_num": 24, "create_time": "2019/1"},
        {"name": "项目3", "interface_num": 25, "create_time": "2019/1"},
    ]
    flash('欢迎来到首页')
    flash('孤鹰')
    return render_template(
        'index.html',p=projects, title='柠檬班', msg='欢迎来到首页'
    )


if __name__ == '__main__':
    app.run(debug=True)