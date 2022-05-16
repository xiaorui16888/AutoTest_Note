# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：test_product.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/10 11:39
"""


class TestProduct:
    def test_product(self, pm, exec_database_sql):
        print('test_product===' + pm, exec_database_sql)
