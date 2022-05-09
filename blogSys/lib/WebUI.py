# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：WebUI.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/8 15:15
"""
from selenium import webdriver
from hytest import *
from selenium.webdriver.common.by import By


def open_browser():
    INFO('打开浏览器')
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    STEP(1, '打开浏览器')
    wd = webdriver.Chrome(options=options)
    wd.implicitly_wait(10)
    GSTORE['wd'] = wd


def mgr_login():
    wd = GSTORE['wd']
    wd.get('http://guoxiaorui.cn/admin')
    wd.find_element(By.ID, 'name').send_keys('guoxiaorui')
    wd.find_element(By.ID, 'password').send_keys('17612917750.')
    wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
