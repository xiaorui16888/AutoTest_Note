# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：管理员登录.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/9 1:47
"""

import sys
from time import sleep

sys.path.append('../')
from blogSys.lib.WebUI import *


class c0008x:
    ddt_cases = []
    for i in range(10):
        ddt_cases.append({
            'name': f'登录 UI_000{i + 1}',
            'para': [i + 1]
        })

    def teststeps(self):
        word = self.para
        print(word)

# 数据驱动，多个用例
class c00003x:
    ddt_cases = [
        {
            'name': '登录 - 000031',
            'para': ['guoxiaorui', None, '请输入密码']
        },
        {
            'name': '登录 - 000032',
            'para': [None, None, '请输入用户名请输入密码']
        },
        {
            'name': '登录 - 000033',
            'para': [None, 'guoxiaorui', '请输入用户名']
        },
        {
            'name': '登录 - 000034',
            'para': ['guoxiaorui', '123456', '用户名或密码无效']
        },
        {
            'name': '登录 - 000035',
            'para': ['guoxiaorui', '17612917750.', '']
        }
    ]

    # 每个用例调用时，该用例的参数参数在 self.para 中
    def teststeps(self):
        wd = GSTORE['wd']
        wd.get('http://guoxiaorui.cn/admin')
        # 取出参数
        username, password, info = self.para
        INFO('{0}--{1}--{2}'.format(username, password, info))
        INFO('管理员登录')
        if username is not None:
            wd.find_element(By.ID, 'name').send_keys(username)
        if password is not None:
            wd.find_element(By.ID, 'password').send_keys(password)

        wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        sleep(2)
        popups = wd.find_elements(By.CSS_SELECTOR, 'div[class^="message popup"]')
        if len(popups) > 0:
            CHECK_POINT('弹出提示', info == popups[0].text)
        else:
            CHECK_POINT('弹出提示', info == '')

    def teardown(self):
        wd = GSTORE['wd']
        name_inputs = wd.find_elements(By.ID, 'name')
        password_inputs = wd.find_elements(By.ID, 'password')
        if len(name_inputs) > 0:
            name_inputs[0].clear()
        if len(password_inputs) > 0:
            password_inputs[0].clear()
