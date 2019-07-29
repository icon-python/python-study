#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 15:21
# @Author  : icon
# @File    : models.py
import os

from test.flask12_homework.app import app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(11), unique=True)
    pwd = db.Column(db.String(20), unique=True)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20))
    create_time = db.Column(db.String(20))
    author = db.Column(db.String(10))
    content = db.Column(db.String(140))


def creat_all():
    db.create_all()


# blogs = Blog.query.order_by(Blog.create_time.desc()).limit(20).all()
# print(blogs)
