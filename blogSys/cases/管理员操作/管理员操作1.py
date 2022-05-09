from time import sleep

from hytest import *
from selenium.webdriver.common.by import By

force_tags = ['登录功能', '冒烟测试', 'UI测试']


class UI_0101:
    name = '管理员登录 - 0101'

    # 测试用例步骤
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(2, '获取右侧菜单信息')
        menusEle = wd.find_elements(By.CSS_SELECTOR, 'div[class="operate"]>a[href^=http]')

        menuText = [menu.text for menu in menusEle]
        INFO(menuText)

        STEP(3, '检查菜单栏')
        CHECK_POINT('右侧菜单检查', menuText[:3] == ['guoxiaorui', '登出', '网站'])

# class UI_0102:
#     name = '添加管理员 - 0102'
#
#     # 测试用例步骤
#     def teststeps(self):
#         wd = GSTORE['wd']
#
#         STEP(2, '进入用户管理页面')
#         wd.find_element(By.ID, 'tonav').click()
#         menus1 = wd.find_elements(By.CSS_SELECTOR, 'li[class="menu-li"]')
#         # 点击内容管理
#         menus1[2].click()
#         # 点击用户分配
#         menus1[2].find_elements(By.CSS_SELECTOR, 'ul[class="menu-ul"] li')[6].click()
#
#         STEP(3, '进入新增用户页面')
#         wd.find_element(By.LINK_TEXT, '新增').click()
#
#         # 查找输入框
#         inputs = wd.find_elements(By.CSS_SELECTOR, 'ul[class="typecho-option"] input')
#         # 输入用户信息
#         inputs[0].send_keys('testuser')
#         inputs[1].send_keys('test@qq.com')
#         inputs[2].send_keys('testNickName')
#         inputs[3].send_keys('testpassword')
#         inputs[4].send_keys('testpassword')
#         inputs[5].send_keys('https://www.baidu.com')
#
#         # 点击提交
#         wd.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#
#         # 等待1秒
#         sleep(3)
#
#         STEP(4, '检查添加信息')
#         userItem = wd.find_element(By.CSS_SELECTOR, 'table tbody tr:nth-last-child(1)')
#         fields = userItem.find_elements(By.TAG_NAME, 'td')[2:5]
#         texts = [field.text for field in fields]
#         print(texts)
#
#         excepted = ['testuser', 'testNickName', 'test@qq.com']
#         CHECK_POINT('用户信息和添加内容一致', texts == excepted)
