#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/3 10:06
# @Author  : icon
# @File    : Class_View.py
import os

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(
    __name__,
    static_url_path='/static',
    static_folder='static'
)
back_content = []
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('demo.html')


# @app.route('/upload')
# def upload_file():
#     return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file2():
    if request.method == "GET":
        return render_template('upload.html')
    if request.method == 'POST':
        f = request.files.get('file')
        if not (f and allowed_file(f.filename)):
            return f'图片格式不支持{f.filename.split(".")[1]}'
        if f.filename.__contains__(' '):
            return '不支持文件名包含空格'
        if f.read().__len__() > 10 * 1024 * 1024:  # 10M
            return '文件大小不能超过10M'
        if not f:
            return render_template('upload.html')
        f.seek(0)  # f.read()读取后，重新定义指针到文件开头
        path = os.path.abspath(os.getcwd()) + '/static/'
        for dir, folder, filename in os.walk(path):
            for fn in filename:
                back_content.append(fn)
        i = 1
        while f.filename in back_content:
            f.filename = f.filename.rsplit(".", 1)[0] + str(i) + '.' + f.filename.rsplit(".", 1)[1]
            i += 1
        f.save('static/' + secure_filename(f.filename))
        back_content.append(f.filename)
        bc = sorted(list(set(back_content)))
        return render_template('back_content.html', back_content=bc)


@app.route('/upload/<filename>')
def get_filename(filename):
    return send_from_directory(os.getcwd()+'/static/', filename)


if __name__ == '__main__':
    app.run(debug=True)
