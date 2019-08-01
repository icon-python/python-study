#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/19 8:34
# @Author  : icon
# @File    : forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Length, DataRequired, Regexp, EqualTo


class AddForm(FlaskForm):
    title = StringField(label="文章标题:", render_kw={"class": "form-control form-control-lg"},
                        validators=[DataRequired("标题不可为空")])
    author = StringField(label="作者姓名:", render_kw={"class": "form-control form-control-lg"},
                         validators=[Length(1, 10, message='作者姓名长度为1-10位'), DataRequired("作者姓名不可为空")])
    content = TextAreaField(label="文章内容:", render_kw={"class": "form-control", "rows": 5, "cols": 50},
                            validators=[Length(1, 140, message='文章长度为1-140位'), DataRequired("文章内容不可为空")])
    submit = SubmitField("发布")


class LoginForm(FlaskForm):
    phone = StringField("手机号码", render_kw={"placeholder": "请输入手机号"}, validators=[Regexp(r'^1[3,5,7,8,9]\d{9}$', message='手机号格式错误或不存在'), DataRequired('手机号码不能为空')])
    pwd = PasswordField("密码", render_kw={"placeholder": "请输入密码"}, validators=[Length(6, 32, '账号不存在或密码错误'), DataRequired('密码不能为空')])
    submit = SubmitField("登录")


class RegisterForm(FlaskForm):
    phone = StringField("手机号码", render_kw={"placeholder": "请输入手机号"}, validators=[Regexp(r'^1[3,5,7,8,9]\d{9}$', message='手机号格式错误'),
                                                                                 DataRequired('手机号码不能为空')])
    pwd = PasswordField("密码", render_kw={"placeholder": "请输入密码"}, validators=[Length(6, 32, '密码长度不对'), DataRequired('密码不能为空')])
    confirm_pwd = PasswordField("确认密码", render_kw={"placeholder": "请再次输入密码"}, validators=[EqualTo('pwd', message='密码确认错误')])
    submit = SubmitField("注册")
