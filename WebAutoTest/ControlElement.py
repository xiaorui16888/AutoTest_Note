# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：ControlElement.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/5 14:57
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
driver.get('http://tools.guoxiaorui.cn/testdemo.html')

# 键入账号
accountInput = driver.find_element(By.ID, 'name')
# 我们假装需要清空输入框
accountInput.clear()
# 输入新字符串
accountInput.send_keys('admin')

# 获取元素的文本内容
logoElement = driver.find_element(By.CLASS_NAME, 'i-logo')
print(logoElement.text)

# 获取元素的属性
print(accountInput.get_attribute('class'))

# 获取元素对应的html文本内容
print(logoElement.get_attribute('outerHTML'))
# 获取元素内部的html文本内容
print(logoElement.get_attribute('innerHTML'))

# 获取输入框里面的文字
inputElement = driver.find_element(By.ID, 'text')
print(inputElement.text)
print(inputElement.get_attribute('innerText'))
print(inputElement.get_attribute('textContent'))
