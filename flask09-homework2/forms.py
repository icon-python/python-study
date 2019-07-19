#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/19 8:34
# @Author  : icon
# @File    : forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired


class AddForm(FlaskForm):
    title = StringField(label="文章标题:", render_kw={"class":"form-control form-control-lg"}, validators=[DataRequired("标题不可为空")])
    author = StringField(label="作者姓名:", render_kw={"class":"form-control form-control-lg"}, validators=[Length(1,10,message='手机号长度为1-10位'),  DataRequired("作者姓名不可为空")])
    content = TextAreaField(label="文章内容:", render_kw={"class":"form-control", "rows":5, "cols":50}, validators=[Length(1,140,message='文章长度为1-140位'), DataRequired("文章内容不可为空")])
    submit = SubmitField("发布")