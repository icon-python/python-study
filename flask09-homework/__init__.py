#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/17 11:23
# @Author  : icon
# @File    : __init__.py.py
import time
blogs = [
    {"id": "1", "title": "文章1", "create_time": int(time.time())+1, "author": "tom", "content": "文章内容"},
    {"id": "2", "title": "文章2", "create_time": int(time.time())+2, "author": "tom", "content": "文章内容"},
    {"id": "3", "title": "文章3", "create_time": int(time.time())+3, "author": "tom", "content": "文章内容"},
]
blogs=sorted(blogs, key=lambda lis: lis["create_time"], reverse=True)[:2]
print(blogs)