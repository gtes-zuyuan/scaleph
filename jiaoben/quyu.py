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

# 点击系统管理系统区域信息，编辑区域
select_b16=brower.find_element_by_css_selector(".accordion h1:nth-child(17)").click()
select_b17=brower.find_element_by_css_selector(".accordion h1:nth-child(17) + div h2:nth-child(5)").click()
select_b18=brower.find_element_by_css_selector(".accordion h1:nth-child(17) + div h2:nth-child(5) + div h3:nth-child(2)").click()

#进入iframe页面
iframe = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe)

#点击新增按钮新增区域
select_b19=brower.find_element_by_css_selector(".location_R li:first-child").click()

#2次进入iframe页面
iframe2 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe2)

#点击新增按钮新增区域并且赋值
select_b20=brower.find_element_by_css_selector("#txtAreaName")
select_b20.send_keys("二监区")

#点击排序号并且赋值
select_b21=brower.find_element_by_css_selector("#txtOrder")
select_b21.send_keys("2")

#勾选是否监区
#select_b22=brower.find_element_by_css_selector(".srk_text1").click()

#退出iframe
brower.switch_to.default_content()
iframe3 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe3)

#保存
select_b22=brower.find_element_by_css_selector("div.ui_buttons input:first-child").click()
time.sleep(1)

#点击房间信息
brower.switch_to.default_content()
select_b23=brower.find_element_by_css_selector(".accordion h1:nth-child(17) + div h2:nth-child(5) + div h3:nth-child(1)").click()

#进入iframe页面
iframe = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe)

#点击新增按钮
select_b24=brower.find_element_by_css_selector(".location_R li:nth-child(1)").click()


# #2次进入iframe页面
iframe2 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe2)

# #编辑房间信息，点击选择（监室）
select_b25=brower.find_element_by_css_selector(".editPageTable tr:nth-child(1)").click()
select_b26=brower.find_element_by_css_selector(".editPageTable tr:nth-child(1) td.fieldInput select option:nth-child(2)").click()

# #编辑房间编号，并且赋值（0202）
select_b27=brower.find_element_by_css_selector("#txtRoomNo")
select_b27.send_keys("0202")


# #编辑房间名称，并且赋值（0202）
select_b28=brower.find_element_by_css_selector("#txtRoomName")
select_b28.send_keys("0202")

# #编辑房间设备号，并且赋值（0202）
select_b29=brower.find_element_by_css_selector("#txtDeviceID")
select_b29.send_keys("0202")

# #点击区域，并且选择（二监区）
select_b30=brower.find_element_by_css_selector("#ddlArea").click()
select_b31=brower.find_element_by_css_selector("#ddlArea option:nth-child(4)").click()

# #点击主管警员，并且选择（陈大牛）
select_b32=brower.find_element_by_css_selector("#ddlPolice1").click()
select_b33=brower.find_element_by_css_selector("#ddlPolice1 option:nth-child(3)").click()

# #点击房间类型，并且选择（单人监室）
select_b34=brower.find_element_by_css_selector("#ddlRoomType").click()
select_b35=brower.find_element_by_css_selector("#ddlRoomType option:nth-child(8)").click()

# #点击风险等级，并且选择（风险一级）
select_b36=brower.find_element_by_css_selector("#ddlRiskLevel").click()
select_b37=brower.find_element_by_css_selector("#ddlRiskLevel option:nth-child(2)").click()

# #勾选是否单人监室
select_b38=brower.find_element_by_css_selector("#cboIsSeparatePersonRoom").click()

# #退出一层iframe
brower.switch_to.default_content()
iframe3 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe3)


# #点击保存
search_b39=brower.find_element_by_css_selector("div.ui_buttons input:first-child").click()

