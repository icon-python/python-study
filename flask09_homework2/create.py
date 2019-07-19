#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 20:31
# @Author  : icon
# @File    : create.py
from _datetime import datetime
import time
with open('blogs.txt', 'r+', encoding='utf-8') as f:
    blogs = eval(f.read())
length = len(blogs)
for i in range(1, length+1):
    add_dict = {'id': length+i, 'title': '文章%s'%i, 'create_time': datetime.fromtimestamp(int(time.time())+i),
                'author': 'tom', 'content': '文章内容'}
    blogs.append(add_dict)
print(blogs)