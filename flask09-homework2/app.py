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
from flask import Flask, render_template, request, jsonify, url_for, redirect, abort, Response, flash

app = Flask(__name__)
app.secret_key = os.getenv("SECRET KEY", 'ss')
with open('blogs.txt', 'r', encoding='utf-8') as f:
    blogs = eval(f.read())


@app.route('/')
@app.route('/blog/', methods=["GET", "POST"])
def blog():
    if request.method == "GET":
        return render_template("blog.html", blogs=sorted(blogs, key=lambda lis: lis["create_time"], reverse=True)[:20],
                               per_page=20)
    if request.method == "POST":
        title = request.form.get('search')
        try:
            bid = [blog["id"] for blog in blogs if blog["title"]==title][0]
            return redirect(url_for('blog_id', bid=bid))
        except:
            abort(400)


@app.route('/blog/<int:bid>', methods=["GET", "POST"])
def blog_id(bid):
    if bid > len(blogs):
        # response = Response(render_template('error400.html', msg="不存在该文章"), status=400,
        #                     content_type="text/html;charset=utf-8")
        # abort(response)
        abort(400)
    if request.method in ["GET", "POST"]:
        return render_template('blog_bid.html', blog=blogs[bid - 1])


@app.route('/blog/add', methods=["GET", "POST"])
def blog_add():
    if request.method == "GET":
        return render_template("blog_add.html")
    title = request.form.get("title")
    author = request.form.get("author")
    content = request.form.get("content")
    if validator_content(content):
        if validator_author(author):
            blogs.append(dict(id=len(blogs) + 1,
                              title=title,
                              author=author,
                              content=content,
                              create_time=str(datetime.fromtimestamp(int(time.time())))
                              ))
            with open('blogs.txt', 'w+', encoding='utf-8') as f:
                f.write(str(blogs))
            return redirect(url_for('success', title=title))
        else:
            flash("作者字数不能超过10且不能为空")
    else:
        flash("字数不能大于等于140且不能为空")
    return redirect(url_for('blog_add'))


@app.errorhandler(400)
def error400(e):
    return render_template("error400.html", msg="不存在该文章"),400


def validator_content(content):
    if len(content) in range(1, 140):
        return True
    return False


def validator_author(author):
    if len(author) in range(1, 10):
        return True
    return False


@app.context_processor
def add_ctc():
    def format_time(timestamp):
        return str(datetime.fromtimestamp(timestamp))

    return {'format_time': format_time, 'temp_var': 20}


@app.route('/blog/add/success/<title>')
def success(title):
    # title = request.args.get('title')
    return render_template('success.html', title=title)


@app.route('/test')
def tes():
    return render_template('test.html', blogs=sorted(blogs, key=lambda lis: lis["create_time"], reverse=True)[:20])


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
