# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：OpenBaidu.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/5 9:14
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

# 创建WebDriver对象，指明使用Chrome浏览器驱动
driver = webdriver.Chrome(options=options)
# 调用WebDriver对象的get方法，打开网址
driver.get('https://www.baidu.com')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
input_element = driver.find_element(By.ID, 'kw')
# 键入python字符串到输入框里
input_element.send_keys('python')
