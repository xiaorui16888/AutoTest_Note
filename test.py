# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/8 16:19
"""

global a


def test1():
    global a
    a = 8
    print(a)


def test2():
    print(a)


if __name__ == '__main__':
    test1()
    test2()
    print(a)
