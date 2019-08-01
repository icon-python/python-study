#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/17 11:23
# @Author  : icon
# @File    : app.py
"""
实现一个类似微博或者 twitter 的内容展示系统，具备以下功能：

提交代码目录结构截图，代码文件，和展示效果小视频。

1、展示最近的 20 条信息，包含内容和作者，以及创建时间（字符串格式）；
2、首页添加一条微博功能，字数少于 140 字。作者名字长度少于10字，创建时间为服务器时间戳，数据通过 flask-sqlalchemy 存储到数据库。
3、用户注册和登录功能。（注册的密码先用明文存储），只有登录了才能发布新微博。
4、如果用户未登录，首页只显示最近 5 条信息。
5.实现 user 表的关注和粉丝功能：
    1、进入用户页面，显示用户的名称，粉丝数量和关注者数量
    2、 点击粉丝数可以查看所有粉丝的名字。
    3、点击关注者数量可以查看所有关注者的数量。
"""

from _datetime import datetime
import time
from flask import Flask, render_template, request, url_for, redirect, abort, session, flash, jsonify
from test.flask13_homework.forms import AddForm, LoginForm, RegisterForm

app = Flask(__name__)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

app.secret_key = os.getenv("SECRET KEY", 'ss')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)


class Follow(db.Model):
    fans_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followers_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(11), unique=True)
    pwd = db.Column(db.String(20))
    fanses = db.relationship('Follow', foreign_keys=[Follow.followers_id],
                             backref=db.backref('followers', lazy='joined'), lazy='dynamic')
    followers = db.relationship('Follow', foreign_keys=[Follow.fans_id], backref=db.backref('fans', lazy='joined'),
                                lazy='dynamic')


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20))
    create_time = db.Column(db.String(20))
    author = db.Column(db.String(10))
    content = db.Column(db.String(140))


@app.route('/get_fans_followers', methods=["GET", "POST"])
def get_fans_followers():
    phone = session.get('phone')
    if request.method == "GET":
        if phone:
            user = User.query.filter_by(phone=phone).first_or_404()
            fans = [f.fans_id for f in user.fanses]
            followers = [f.followers_id for f in user.followers]
            return jsonify({'fans': fans, 'followers': followers})
        else:
            return jsonify({'fans': 0, 'followers': 0})
    else:
        if phone:
            user = User.query.filter_by(phone=phone).first_or_404()
            fans = [f.fans_id for f in user.fanses]
            followers = [f.followers_id for f in user.followers]
            fans_phone = [User.query.filter_by(id=fid).first_or_404().phone for fid in fans]
            followers_phone = [User.query.filter_by(id=fid).first_or_404().phone for fid in followers]
            return jsonify({'fans': fans_phone, 'followers': followers_phone})
        else:
            return jsonify({'fans': 0, 'followers': 0})


def decorator_login(func):
    def decorator(*args, **kwargs):
        if 'phone' in session:
            res = func(*args, **kwargs)
            return res
        else:
            return redirect(url_for('login'))

    return decorator


@app.route('/')
@app.route('/login', methods=["GET", "POST"], endpoint='login')
def login():
    if request.method == "GET":
        return render_template('login.html', login_form=LoginForm())
    else:
        login_form = LoginForm(request.form)
        phone = request.form.get('phone')
        pwd = request.form.get('pwd')
        phone_db = User.query.filter_by(phone=phone).first()
        if login_form.validate() and phone_db is not None:
            if pwd == phone_db.pwd and phone_db.phone:
                session['phone'] = phone
                return redirect(url_for('blog'))
            else:
                return render_template('login.html', login_form=LoginForm())
        else:
            if not phone_db:
                flash('该手机号尚未注册')
            return render_template('login.html', login_form=login_form)


@app.route('/register', methods=["GET", "POST"], endpoint='register')
def register():
    if request.method == "GET":
        return render_template('register.html', register_form=RegisterForm())
    else:
        register_form = RegisterForm(request.form)
        if register_form.validate_on_submit():
            phone = request.form.get('phone')
            pwd = request.form.get('pwd')
            new_user = User(phone=phone, pwd=pwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html', register_form=register_form)


@app.route('/blog', methods=["GET", "POST"], endpoint='blog')
def blog():
    if request.method == "GET":
        if 'phone' in session:
            blogs = Blog.query.order_by(Blog.create_time.desc()).limit(20).all()
            return render_template("blog.html", blogs=blogs, phone=session['phone'])
        else:
            blogs = Blog.query.order_by(Blog.create_time.desc()).limit(5).all()
            return render_template("blog.html", blogs=blogs, phone=0)
    if request.method == "POST":
        title = request.form.get('search')
        b = Blog.query.filter_by(title=title).first_or_404()
        return redirect(url_for('blog_id', bid=b.id))


@app.route('/blog/<int:bid>', methods=["GET", "POST"], endpoint='blog_id')
@decorator_login
def blog_id(bid):
    if request.method == "GET":
        blogs = Blog.query.filter_by(id=bid).first_or_404()
        return render_template('blog_bid.html', blog=blogs)
    if request.method == "POST":
        title = request.form.get('title')
        blogs = Blog.query.filter_by(title=title).first_or_404()
        return render_template('blog_bid.html', blog=blogs)


@app.route('/blog/add', methods=["GET", "POST"], endpoint='blog_add')
@decorator_login
def blog_add():
    if request.method == "GET":
        return render_template("blog_add.html", form=AddForm())
    if request.method == "POST":
        form = AddForm(request.form)
        if form.validate_on_submit():
            create_time = str(datetime.fromtimestamp(int(time.time())))
            new_blog = Blog(title=form.title.data, author=form.author.data, content=form.content.data,
                            create_time=create_time)
            db.session.add(new_blog)
            db.session.commit()
            b = Blog.query.filter_by(create_time=create_time).first()
            return redirect(url_for('blog_id', bid=b.id))
        else:
            return render_template("blog_add.html", form=form)


@app.route('/blog/add/success/<title>', endpoint='success')
@decorator_login
def success(title):
    return render_template('success.html', title=title)


@app.errorhandler(404)
def error404(e):
    return render_template("error404.html", msg="不存在该文章"), 404


@app.context_processor
def add_ctc():
    def format_time(timestamp):
        return str(datetime.fromtimestamp(timestamp))

    return {'format_time': format_time, 'temp_var': 20}


@app.route('/test')
def t():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
    # app.run(debug=True)
