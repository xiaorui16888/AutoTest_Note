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
driver.get('http://tools.guoxiaorui.cn/testdemo2.html')

# 先切换到需要操作元素所属的frame元素内---属性name值或id值
driver.switch_to.frame('frame1')

# 也可以填写frame 所对应的 WebElement 对象，不过这种写法过于麻烦了~
# driver.switch_to.frame(driver.find_element(By.TAG_NAME, 'iframe'))

plantElements = driver.find_elements(By.CLASS_NAME, 'plant')
for plant in plantElements:
    print(plant.text)

# 切换到原来的主html
driver.switch_to.default_content()
driver.find_element(By.ID, 'outerbutton').click()
