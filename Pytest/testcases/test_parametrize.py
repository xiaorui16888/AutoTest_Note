# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：test_parametrize.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/10 20:34
"""
import pytest


class TestParametrize:

    @pytest.mark.smoke
    @pytest.mark.parametrize('caseInfo', ['小明', '小王', '小灰'])
    def test_01(self, caseInfo):
        print(caseInfo)

    @pytest.mark.smoke
    @pytest.mark.parametrize('name,age', [['小明', '21'], ['小王', '22'], ['小林', '23']])
    def test_02(self, name, age):
        print(name, age)
