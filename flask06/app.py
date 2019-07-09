#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 18:22
# @Author  : icon
# @File    : app.py
import json
import os

from flask import Flask, request, make_response, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # return  json.dumps({"user":"admin"}),{"content-type":"application/json"}
        # resp = make_response(json.dumps({"user":"admin2"}),{"content-type":"application/json"})
        # resp.status = '202'
        # resp.content_type = 'text/html'
        # resp = jsonify({"user":"阿丽塔"})
        # return resp
        return render_template("index.html")


@app.route('/upload', methods=["POST"])
def upload():
    if request.method == "POST":
        a = request
        print(a.content_type)
        f = request.files.get('pic')
        f.save('static/'+secure_filename(f.filename))
        return "success"


@app.route('/upload/<filename>')
def get_filename(filename):
    return send_from_directory(os.getcwd()+'/static/', filename)


if __name__ == '__main__':
    app.run(debug=True)
