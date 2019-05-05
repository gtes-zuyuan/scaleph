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

#点击综合管理下拉菜单在押人员管理
select_h1=brower.find_element_by_css_selector(".accordion h1").click()
select_h2=brower.find_element_by_css_selector(".accordion h2").click()

#进入iframe,使用标签进行定位
iframe = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe)

#点击新增按钮
select_h3=brower.find_element_by_css_selector(".location_R li:first-child").click()

#再次进入iframe页面
iframe2 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe2)

#编辑在押人员信息，人员编号赋值
select_h4=brower.find_element_by_css_selector("#txtNo")
select_h4.send_keys("03")

#编辑在押人员信息，姓名赋值
select_h5=brower.find_element_by_css_selector("#txtName")
select_h5.send_keys("haha")

#点击所在区域选择所在监区
select_h6=brower.find_element_by_css_selector(".editPageTable tr:nth-child(7)").click()
time.sleep(1)
select_h7=brower.find_element_by_css_selector(".editPageTable tr:nth-child(7) td.fieldInput select option:nth-child(3)").click()

#点击所在监视择监视
select_h8=brower.find_element_by_css_selector(".editPageTable tr:nth-child(8)").click()
time.sleep(1)
select_h9=brower.find_element_by_css_selector(".editPageTable tr:nth-child(8) td.fieldInput select option:nth-child(3)").click()

#退出iframe标签
brower.switch_to.default_content()
iframe3 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe3)

#点击保存按钮并且保存并且退出到最外层
select_h10=brower.find_element_by_css_selector("div.ui_buttons input:first-child").click()
brower.switch_to.default_content()
time.sleep(1)

#点击系统管理下拉菜单兄弟元素以及民警管理下拉菜单民警信息
select_b1=brower.find_element_by_css_selector(".accordion h1:nth-child(17)").click()
select_b2=brower.find_element_by_css_selector(".accordion h1:nth-child(17) + div h2:nth-child(3)").click()
select_b3=brower.find_element_by_css_selector(".accordion h1:nth-child(17) + div h2:nth-child(3) + div h3:first-child").click()

#进入iframe页面
iframe = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe)


#点击新增按钮
select_b4=brower.find_element_by_css_selector(".location_R li:first-child").click()

#再次进入iframe页面
iframe2 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe2)


#编辑民警信息 姓名框并且赋值
select_b5=brower.find_element_by_css_selector("#txtName")
select_b5.send_keys("陈大牛")

#编辑民警信息 编号框并且赋值
select_b6=brower.find_element_by_css_selector("#txtPoliceNumber")
select_b6.send_keys("8888")

#编辑民警信息性别 选择性别 女性
select_b7=brower.find_element_by_css_selector("#rdbFemale").click()

#点击职位并且选择职位（民警）
select_b8=brower.find_element_by_css_selector(".editPageTable tr:nth-child(4)").click()
# select_b9=brower.find_element_by_css_selector("#ddlPosition option:nth-child(10)").click()
select_b9=brower.find_element_by_css_selector(".editPageTable tr:nth-child(4) td.fieldInput select option:nth-child(10)").click()
select_b10=brower.find_element_by_css_selector(".editPageTable tr:nth-child(4)").click()

#点击警衔并且选择见习警员
select_b11=brower.find_element_by_css_selector("#ddlPoliceRank").click()
select_b12=brower.find_element_by_css_selector("#ddlPoliceRank option:nth-child(15)").click()
select_b13=brower.find_element_by_css_selector("#ddlPoliceRank").click()

#编辑民警电话并且赋值
select_b14=brower.find_element_by_css_selector("#txtPhone")
select_b14.send_keys("123456789101")


#选择文件
#select_b11=brower.find_element_by_css_selector("#fileImage").click()
#上传照片

# 切换出一层iframe：一共2层，只需要切换出一层即可
brower.switch_to.default_content()
iframe3 = brower.find_elements_by_tag_name("iframe")[0]
brower.switch_to.frame(iframe3)


#点击保存按钮进行保存
select_b12=brower.find_element_by_css_selector("div.ui_buttons input:first-child").click()




