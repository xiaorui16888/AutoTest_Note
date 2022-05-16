# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：conftest.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/10 11:29
"""
import pytest


def read_yaml():
    return ['111', '222', '333']


# #autouse自动执行，无需给方法传递参数
# @pytest.fixture(scope='function',autouse=True)
@pytest.fixture(scope='function', params=read_yaml())
def exec_database_sql(request):
    print(request.param)
    print('执行sql语句')
    yield request.param
    print('关闭数据库连接')
