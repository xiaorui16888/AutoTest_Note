# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：FrameControl.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/6 0:20
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
driver.get('http://tools.guoxiaorui.cn/testdemo3.html')

# mainWindow变量保存当前窗口的句柄
mainWindow = driver.current_window_handle

link = driver.find_element(By.LINK_TEXT, '访问bing网站')
link.click()

for handle in driver.window_handles:
    # 先切换到该窗口
    driver.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '必应' in driver.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

driver.find_element(By.ID, 'sb_form_q').send_keys('test')

# 切换到新窗口操作完后，切换到老窗口
# 通过前面保存的老窗口的句柄，自己切换到老窗口
driver.switch_to.window(mainWindow)
