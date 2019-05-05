##coding:utf-8 指定编码格式

#导入浏览器驱动
from selenium import webdriver
import time


#进入网站  新增在押人员管理和民警信息
brower=webdriver.Chrome()
url="http://localhost:8004/"
brower.get (url)

#窗口最大化
brower.maximize_window()

#点击用户名输入框并且给予赋值
select_name=brower.find_element_by_css_selector("#txtLoginName")
select_name.clear()
select_name.send_keys("admin")

#点击密码输入框并且给予赋值
select_name=brower.find_element_by_css_selector("#txtLoginPass")
select_name.clear()
select_name.send_keys("admin+123")

#点击登录按钮
select_btn=brower.find_element_by_css_selector("#btnLogin").click()
time.sleep(1)



