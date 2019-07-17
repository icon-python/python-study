#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/17 11:23
# @Author  : icon
# @File    : app.py
"""
实现一个类似微博或者 twitter 的内容展示系统，具备以下功能：

提交代码目录结构截图，代码文件，和展示效果小视频。

1、展示最近的 20 条信息，包含内容和作者，以及创建时间（字符串格式）；
2、创建一条微博功能，字数少于 140 字。作者名字长度少于10字，创建时间为服务器时间戳
3、使用脚本生成 20 条数据， 包含内容和作者，以及创建时间，在前端展示出来；
4、数据保存到 sqlite 数据库（选做，不做要求）
"""
import os
from _datetime import datetime
import time
from flask import Flask, render_template, request, jsonify, url_for, redirect, current_app, abort, Response, flash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET kEY", 'ss')
blogs = [
    {"id": "1", "title": "文章1", "create_time": "2019-07-17 16:17", "author": "tom", "content": "文章内容"},
    {"id": "2", "title": "文章2", "create_time": "2019-07-17 16:18", "author": "tom", "content": "文章内容"},
    {"id": "3", "title": "文章3", "create_time": "2019-07-17 16:19", "author": "tom", "content": "文章内容"},
]


@app.route('/')
@app.route('/blog', methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return render_template("blog.html", blogs=sorted(blogs, key=lambda lis: lis["create_time"], reverse=True)[:2])
    # response = Response(render_template('error400.html', msg="不支持当前请求方式"), status=400,
    #                     content_type="text/html;charset=utf-8")
    # abort(response)


@app.route('/blog/add', methods=["GET", "POST"])
def blog_add():
    if request.method == "GET":
        return render_template("blog_add.html")
    title = request.form.get("title")
    author = request.form.get("author")
    content = request.form.get("content")
    if validator_content(content):
        if validator_author(author):
            blogs.append(dict(id=len(blogs)+1,
                              title=title,
                              author=author,
                              content=content,
                              create_time=datetime.fromtimestamp(int(time.time()))
                              ))
            return render_template('success.html', title=title)
        else:
            flash("作者字数不能超过10且不能为空")
    else:
        flash("字数不能大于等于140且不能为空")
    return redirect(url_for('blog_add'))


def validator_content(content):
    if len(content) in range(1, 140):
        return True
    return False


def validator_author(author):
    if len(author) in range(1, 10):
        return True
    return False


@app.route('/getblog/<int:id>')
def get_blog(id):
    return jsonify({"id": id, "title": "title"})


# @app.route('/favicon.ico')
# def favicon():
#     # 后端返回文件给前端（浏览器），send_static_file是Flask框架自带的函数
#     return current_app.send_static_file('static/image/favicon.ico')
@app.context_processor
def add_ctc():
    def format_time(timestamp):
        return str(datetime.fromtimestamp(timestamp))

    return {'format_time': format_time, 'temp_var': 20}


if __name__ == '__main__':
    app.run(debug=True)
