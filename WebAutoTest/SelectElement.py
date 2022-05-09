# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：SelectElement.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/6 0:58
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

# 创建WebDriver对象，指明使用Chrome浏览器驱动
driver = webdriver.Chrome(options=options)
# 隐式等待
driver.implicitly_wait(10)
# 调用WebDriver对象的get方法，打开网址
driver.get('http://tools.guoxiaorui.cn/testdemo4.html')

# 获取当前选中的元素
checkedElement = driver.find_element(By.CSS_SELECTOR, '#s_radio input[checked=checked]')
print('当前选中：' + checkedElement.get_attribute('value'))

# 点击选中小江老师
driver.find_element(By.CSS_SELECTOR, '#s_radio input[value="小江老师"]').click()

# 点击选中的选项
checkedElements = driver.find_elements(By.CSS_SELECTOR, '#s_checkbox input[checked=checked]')

for element in checkedElements:
    element.click()

driver.find_element(By.CSS_SELECTOR, '#s_checkbox input[value="小江老师"]').click()

# 创建select对象
singleSelect = Select(driver.find_element(By.ID, 'ss_single'))
# 通过select对象选中小江老师
singleSelect.select_by_visible_text('小江老师')

# 创建select对象
multipleSelect = Select(driver.find_element(By.ID, 'ss_multi'))
# 清除所以 已经选中的 选项
multipleSelect.deselect_all()
# 选中需要选择的
multipleSelect.select_by_visible_text('小江老师')
multipleSelect.select_by_visible_text('小雷老师')
