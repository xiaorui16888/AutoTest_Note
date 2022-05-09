# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：__st__.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/8 17:03
"""
import sys

sys.path.append('../')
from blogSys.lib.WebUI import *


def suite_setup():
    mgr_login()
