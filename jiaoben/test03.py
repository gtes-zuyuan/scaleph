#coding:utf-8 指定编码格式

#导入浏览器驱动
from selenium import webdriver
import time

#进入网站
brower=webdriver.Chrome()
# brower = webdriver.Chrome() 设置了chromedriver的环境变量
url="http://localhost:8004/"
brower.get(url)
#print("open the http://localhost:8004" )

#浏览器最大化
brower.maximize_window()

# 登录-1、找到用户名+赋值
search_name=brower.find_element_by_css_selector("#txtLoginName")
search_name.clear()
search_name.send_keys("admin")

# 登录-2、找到密码+赋值
search_login=brower.find_element_by_css_selector("#txtLoginPass")
search_login.clear()
search_login.send_keys("admin+123")

# 登录-3、点击登录按钮
search_btn=brower.find_element_by_css_selector("#btnLogin")
search_btn.click()
time.sleep(1)


select_b16=brower.find_element_by_css_selector(".accordion h1:nth-child(17)").click()
select_b17=brower.find_element_by_css_selector(".accordion h1:nth-child(17) + div h2:nth-child(5)").click()
select_b18=brower.find_element_by_css_selector(".accordion h1:nth-child(17) + div h2:nth-child(5) + div h3:nth-child(1)").click()

#进入iframe页面
iframe = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe)

#点击新增按钮新增区域
select_b19=brower.find_element_by_css_selector(".location_R li:first-child").click()