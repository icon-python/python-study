#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/3 10:06
# @Author  : icon
# @File    : app.py
import os

from flask import Flask, render_template, request

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static'
)
back_content = []


@app.route('/')
def index():
    return render_template('demo.html')


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/back_content', methods=['GET', 'POST'])
def upload_file2():
    if request.method == 'POST':
        f = request.files['file']
        if not f:
            return render_template('upload.html')
        path = os.path.abspath(os.path.dirname(__file__) + '/static/')
        f.save(path + f.filename)
        for dir, folder, filename in os.walk(path):
            for fn in filename:
                back_content.append(fn)
        bc = sorted(list(set(back_content)))
        return render_template('back_content.html', back_content=bc)


if __name__ == '__main__':
    app.run(debug=True)
