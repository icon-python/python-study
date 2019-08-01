#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 20:31
# @Author  : icon
# @File    : create.py
from _datetime import datetime
import time
from test.flask13_homework.models import *

try:
    blogs = Blog.query.all()
    for i in range(len(blogs) + 1, len(blogs) + 21):
        title = '文章%s' % i
        author = 'tom'
        content = '文章内容'
        create_time = str(datetime.fromtimestamp(int(time.time())))
        new_blog = Blog(title=title, author=author, content=content, create_time=create_time)
        db.session.add(new_blog)
        db.session.commit()
except:
    creat_all()
    for i in range(1, 21):
        title = '文章%s' % i
        author = 'tom'
        content = '文章内容'
        create_time = str(datetime.fromtimestamp(int(time.time())))
        new_blog = Blog(title=title, author=author, content=content, create_time=create_time)
        db.session.add(new_blog)
        db.session.commit()
