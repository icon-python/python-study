#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/7/18 20:22
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Regexp, Length, EqualTo


class RegisterForm(FlaskForm):
    # 表单属性要和前端的name要一直
    # 数据库里面的字段。
    phone = StringField("手机号码", render_kw={"class":"form-control"}, validators=[
        Regexp(r'^1[3,5,7,8,9]\d{9}$', message='手机号码格式错误'),
        DataRequired('手机号码不能为空')])
    pwd = PasswordField("密码", validators=[
        Length(6, 32, '密码长度不对'),
        DataRequired('密码不能为空')])
    confirm_pwd = PasswordField("确认密码", validators=[EqualTo('pwd', message='密码确认错误')])
    job = SelectField('Job', choices=[
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('engineer', 'Engineer'),
        ('lawyer', 'Lawyer')
    ])