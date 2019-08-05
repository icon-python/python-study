#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 21:22
# @Author  : icon
# @File    : config.py

class BaseConfig:
    PER_PAGE = 10
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductConfig(BaseConfig):
    pass

config = DevelopmentConfig()