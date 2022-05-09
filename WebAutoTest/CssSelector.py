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
driver.get('http://tools.guoxiaorui.cn/testdemo.html')

# 通过tag选择
spans = driver.find_elements(By.CSS_SELECTOR, 'span')
for span in spans:
    print(span.text)

# 通过id选择
title = driver.find_element(By.CSS_SELECTOR, '#title')
print(title.text)

# 通过css选择
animals = driver.find_elements(By.CSS_SELECTOR, '.animal')
for animal in animals:
    print(animal.text)

# 子元素选择--多层级
childElement1 = driver.find_element(By.CSS_SELECTOR, 'div > #layer1 > #layer1_1')
print(childElement1.text)

childElement2 = driver.find_element(By.CSS_SELECTOR, 'div > #layer1_1')
print(childElement2.text)

aElement = driver.find_element(By.CSS_SELECTOR, '[href="https://www.baidu.com/"]')
print(aElement.get_attribute('outerHTML'))

aElementContainBaidu = driver.find_element(By.CSS_SELECTOR, '[href*="baidu"]')
print(aElementContainBaidu.get_attribute('outerHTML'))

aElementStartWithHttp = driver.find_element(By.CSS_SELECTOR, '[href^="http"]')
print(aElementStartWithHttp.get_attribute('outerHTML'))

aElementEndWithCOM = driver.find_element(By.CSS_SELECTOR, '[href$="com/"]')
print(aElementEndWithCOM.get_attribute('outerHTML'))

aElementContainGoogle = driver.find_element(By.CSS_SELECTOR,
                                            'a[href*="google"][class="google"]')
print(aElementContainGoogle.get_attribute('outerHTML'))
