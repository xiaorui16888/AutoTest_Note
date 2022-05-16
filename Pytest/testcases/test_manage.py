# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：test_manage.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/10 11:31
"""


class TestManage:

    def test_add_user(self, exec_database_sql):
        print('test_add_user===添加用户', exec_database_sql)
