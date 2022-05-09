# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：DialogElement.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/6 9:19
"""

# 弹出对话框
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

# 创建WebDriver对象，指明使用Chrome浏览器驱动
driver = webdriver.Chrome(options=options)
# 隐式等待
driver.implicitly_wait(10)
# 调用WebDriver对象的get方法，打开网址
driver.get('http://tools.guoxiaorui.cn/dialog.html')

# alert
driver.find_element(By.ID, 'b1').click()
# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)
# 点击ok按钮
driver.switch_to.alert.accept()

# confirm
driver.find_element(By.ID, 'b2').click()
# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)
# 点击ok按钮
driver.switch_to.alert.accept()
# confirm
driver.find_element(By.ID, 'b2').click()
# 打印 弹出框 提示信息
print(driver.switch_to.alert.text)
# 点击cancel按钮
driver.switch_to.alert.dismiss()

# Prompt
driver.find_element(By.ID, 'b3').click()
alert = driver.switch_to.alert
# 打印 弹出框 提示信息
print(alert.text)
# 输入信息
alert.send_keys('不是')
# 点击cancel按钮
alert.accept()

time.sleep(3)
driver.find_element(By.ID, 'b3').click()
alert = driver.switch_to.alert
alert.dismiss()


