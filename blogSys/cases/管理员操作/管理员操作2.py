from time import sleep

from hytest import *
from selenium.webdriver.common.by import By


class UI_0201:
    name = '管理员登录 - 0201'

    # 测试用例步骤
    def teststeps(self):
        wd = GSTORE['wd']
        STEP(2, '获取右侧菜单信息')
        menusEle = wd.find_elements(By.CSS_SELECTOR, 'div[class="operate"]>a[href^=http]')

        menuText = [menu.text for menu in menusEle]
        INFO(menuText)

        STEP(3, '检查菜单栏')
        CHECK_POINT('右侧菜单检查', menuText[:3] == ['guoxiaorui', '登出', '网站'])
