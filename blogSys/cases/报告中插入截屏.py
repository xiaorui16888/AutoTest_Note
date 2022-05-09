# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：报告中插入截屏.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/9 15:08
"""
import sys

sys.path.append('../')
from blogSys.lib.WebUI import *


class c8:
    name = "报告插入截图"

    def teststeps(self):
        wd = GSTORE['wd']
        wd.get('http://guoxiaorui.cn/admin')
        # 第1个参数是 webdriver 对象
        # width 参数为可选参数， 指定图片显示宽度
        SELENIUM_LOG_SCREEN(wd, width='70%')
        # 插入网络图片
        LOG_IMG('http://guoxiaorui.cn/usr/plugins/SimpleAdmin/static/img/suya.jpg')
        # 插入本地图片
        # LOG_IMG('假装我是本地图片，可以用绝对路径')
