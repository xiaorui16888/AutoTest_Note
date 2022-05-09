# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：FindElement.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/5 9:53
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

# 这里是通过元素的class查找，find_elements会返回一个列表。
plantElements = driver.find_elements(By.CLASS_NAME, 'plant')
# 我们可以通过for循环遍历元素的内容
for plant in plantElements:
    # 打印其text属性的值
    print(plant.text)

# 通过TAG_NAME查询元素
pElements = driver.find_elements(By.TAG_NAME, 'p')
for p in pElements:
    print(p.text)

# 通过WebElement对象选择元素
bodyElement = driver.find_element(By.TAG_NAME, 'body')
spanElements = bodyElement.find_elements(By.TAG_NAME, 'a')
for span in spanElements:
    print(span.text)
