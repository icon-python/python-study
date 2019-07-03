#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/3 10:05
# @Author  : icon
# @File    : __init__.py.py


import os
lis = []
for dir, folder, filename in os.walk(os.getcwd()+'/static/'):
    lis.append(filename)
    print(filename)
# print(*lis)
