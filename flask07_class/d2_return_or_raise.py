#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/7/11 20:50

# def run():
#     def decorator():
#         return
#     return

def run(num) -> int:
    if num > 4:
        raise Exception()
    elif num == 4:
        raise Exception()
    else:
        return num -2

# python 哲学：return ==>  raise

a = run(5)
# if isinstance()
# 函数里面如果有多个 return, return 的类型是一致的。