#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 21:03
# @Author  : icon
# @File    : run.py


from class_dev.dev01.app import create_app

app = create_app()
if __name__ == '__main__':
    print(app.config['DEBUG'])
    app.run(debug=app.config['DEBUG'])
