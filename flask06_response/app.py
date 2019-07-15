#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 18:22
# @Author  : icon
# @File    : manage.py
import json
import os

from flask import Flask, request, make_response, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # return  json.dumps({"user":"admin"}),{"content-type":"application/json"}  # 1.返回中指定类型
        # resp = make_response(json.dumps({"user":"admin2"}),{"content-type":"application/json"})  # 2.使用make_response()
        # resp.status = '202'
        # resp.content_type = 'text/html'  # content_type、mimetype都是指定返回资源类型
        # resp.mimetype = 'application/json'
        # resp = jsonify({"user":"阿丽塔"})  # 3.使用jsonify
        # return resp, 201
        return render_template("index.html")


@app.route('/upload', methods=["POST"])
def upload():
    if request.method == "POST":
        a = request
        print(a.content_type)
        # f = request.files.get('pic')
        # f.save('static/'+secure_filename(f.filename))
        return "success"
    else:
        return "get"


@app.route('/upload/<filename>')
def get_filename(filename):
    return send_from_directory(os.getcwd()+'/static/', filename)


if __name__ == '__main__':
    app.run(debug=True)
