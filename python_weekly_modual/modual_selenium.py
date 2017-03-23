#-*- coding:utf-8 -*-
# 导入 webdriver
from selenium import webdriver

# 打开 chrome 浏览器
driver = webdriver.Chrome()

# 进入百度首页
driver.get('http://www.baidu.com')
# 定位到搜索框，发送文本
textbox = driver.find_element_by_id('kw')
textbox.send_keys('crossin的编程教室')
# 定位 搜索 按钮
buttom = driver.find_element_by_id('su')
# 点击搜索
buttom.click()
