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

#点击综合管理下拉菜单在押人员管理
search_h1=brower.find_element_by_css_selector(".accordion h1").click()
search_h2=brower.find_element_by_css_selector(".accordion h2").click()

#进入iframe页面,使用标签进行定位
iframe = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe)

#点击按新增钮事件
search_h3=brower.find_element_by_css_selector(".location_R li:first-child").click()

#点击新增按钮进行信息填写
#进入iframe页面
iframe2 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe2)
#点击人员编号按钮，并且给它赋值
search_h4=brower.find_element_by_css_selector("#txtNo")
search_h4.send_keys("02")
#点击姓名按钮，并且给它赋值
search_h5=brower.find_element_by_css_selector("#txtName")
search_h5.send_keys("嘻嘻")
#点击下拉框所在区域进行选择
search_h6=brower.find_element_by_css_selector(".editPageTable tr nth-child(7)").click()
search_h7=brower.find_element_by_css_selector(".eitPageTable tr nth-child(7) td.fieldInput select option:nth-child(3)").click()

#点击下拉框所在监视进行选择
search_h8brower.find_element_by_css_selector(".editPageTable tr nth-child(8)").click()
search_h9brower.find_element_by_css_selector(".editPageTable tr nth-child(8) td.fieldInput select option:nth-child(3)").click()
# 切换出一层iframe：一共2层，只需要切换出一层即可
brower.switch_to.default_content()
iframe3 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe3)
# 点击保存按钮
search_h10rower.find_element_by_css_selector("div.ui_buttons input:first-child").click()