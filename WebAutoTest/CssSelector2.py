# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：CssSelector.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/5 23:01
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

# 创建WebDriver对象，指明使用Chrome浏览器驱动
driver = webdriver.Chrome(options=options)
# 隐式等待
driver.implicitly_wait(10)
# 调用WebDriver对象的get方法，打开网址
driver.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

authors=driver.find_elements(By.CSS_SELECTOR,'span:nth-child(2)')
for author in authors:
    print(author.text)