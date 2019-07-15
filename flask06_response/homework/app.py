#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/7/10 10:31
# @Author  : icon
# @File    : app.py
"""
定义以下接口，返回 json 格式数据：（数据可以用列表字典保存到后端）

1、返回所有项目数据，包含：项目id, 项目名称，项目简介，创建时间，修改时间
2、根据id获取单个项目数据。
3、修改单个项目数据。
4、创建项目
5、删除项目

注意： 客户端不管是浏览器还是手机，postman, 只要根据接口文档要求发送了对应的请求，就能操作对应接口的资源。
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
with open('projects.txt', 'r+', encoding="utf-8") as f:
    list_projects = eval(f.read())


@app.route('/projects')
def projects():
    json_data = {"code": "200", "msg": "所有项目", "data": [data for data in list_projects]}
    return jsonify(json_data), '200 OK'


@app.route('/project/<int:id>')
def project(id):
    if id in range(1, len(list_projects) + 1):
        json_data = {"code": "200", "msg": list_projects[id - 1]["pro_name"],
                     "data": [list_projects[id - 1]]}
        return jsonify(json_data), '200 OK'
    else:
        json_data = {"code": "400", "msg": "不存在该项目", "data": ""}
        return jsonify(json_data), '201 OK'


@app.route('/project_edit/<int:id>')
def project_edit(id):
    if id in range(1, len(list_projects) + 1):
        req = request.args
        for k, v in req.items():
            if k in list_projects[id-1]:
                list_projects[id - 1][k] = v
                with open('projects.txt', 'w+', encoding="utf-8") as f:
                    f.write(str(list_projects))
            else:
                return jsonify({"msg": "该项目不存在该参数{}".format(k)}), "201 OK"
        return jsonify({"code": "200", "msg": "修改成功"}), "200 OK"
    return jsonify({"code": "400", "msg": "不存在该项目，编辑失败", "data": ""}), "201 OK"


@app.route('/project_add/<int:id>')
def project_add(id):
    if id not in range(1, len(list_projects) + 1):
        req = request.args
        list_projects.append(req.to_dict())
        with open('projects.txt', 'w+', encoding="utf-8") as f:
            f.write(str(list_projects))
        return jsonify({"code": "200", "msg": "新增项目成功"}), "200 OK"
    else:
        return jsonify({"msg": "该项目已存在，新增失败"}), "201 OK"


@app.route('/project_del/<int:id>')
def project_del(id):
    if id in range(1, len(list_projects) + 1):
        list_projects.pop(id - 1)
        with open('projects.txt', 'w+', encoding="utf-8") as f:
            f.write(str(list_projects))
        return jsonify({"code": "200", "msg": "删除项目成功"}), "200 OK"
    else:
        return jsonify({"msg": "该项目不存在，删除失败"}), "201 OK"


if __name__ == '__main__':
    app.run(debug=True)
