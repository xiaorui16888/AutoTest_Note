# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：MoreAndMoreAction.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/6 9:32
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 手机模式

# 设置手机型号，这设置为iPhone 6
mobile_emulation = {"deviceName": "iPhone 6"}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

# 启动配置好的浏览器
driver = webdriver.Chrome(options=options)

# 输入网址
driver.get('http://m.baidu.com')
# 截屏保存为图片文件
driver.get_screenshot_as_file('error.png')
