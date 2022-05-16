# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：conftest.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/10 11:39
"""
import pytest


@pytest.fixture(scope='function', autouse=False, name='pm')
def product_manage():
    print('执行sql查询')
    yield 'success'
    print('关闭数据库连接')
