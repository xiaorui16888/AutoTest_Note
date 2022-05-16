# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：run.py.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/9 18:01
"""
import os
from time import sleep

import pytest

if __name__ == '__main__':
    pytest.main()
    # sleep(3)
    # os.system('allure generate ./temps -o ./reports --clean')
