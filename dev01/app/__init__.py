#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 21:20
# @Author  : icon
# @File    : __init__.py


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from class_dev.dev01.app.config import config
app = Flask(__name__)
# db = SQLAlchemy()
# 其它地方是有app，就不需要显示调用app对象，因为app启动后，有上下文环境后，可以通过app代理对象current_app来操作app。
def create_app():
    app.config.from_object(config)
    # db.init_app(app)
    return app
