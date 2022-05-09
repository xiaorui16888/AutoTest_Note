# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：MoreAction.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/6 8:51
"""

# 其余的一些动作--实战技巧

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
driver.get('https://www.baidu.com')

action = ActionChains(driver)
# 鼠标移动到 元素上
action.move_to_element(driver.find_element(By.CSS_SELECTOR, '[name="tj_briicon"]')).perform()


