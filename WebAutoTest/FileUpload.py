# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：FileUpload.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/6 10:18
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
driver.get('https://tinypng.com/')

# 先定位到上传文件的元素
uploadElement = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
# 添加文件
uploadElement.send_keys(r'C:\Users\Administrator\Desktop\logo.png')
