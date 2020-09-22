# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url='https://club.geely.com/personalCenter/personalProfile')
#检查页面是否有同意cookie选项
button = browser.find_elements_by_class_name("knoweButton")
if len(button)!=0:
    # 点击一下同意
    print("点击了一下同意cookie")
    browser.execute_script("arguments[0].click();", button[0])
button = browser.find_elements_by_xpath("html/body/div/div/div/button")
if len(button)==0:
    print("没有找到跳转登陆按钮")
    browser.close()
button[0].click()
# 跳转登陆
# button = browser.find_elements_by_class_name("sign")
# if len(button)==0:
#
#     browser.close()
# button[0].click()
# time.sleep(2)
# 输入账号密码
inputs = browser.find_elements_by_class_name("step")
if len(button)<2:
    print("没有找到输入框")
    browser.close()
#手机号
inputs[0].send_keys("*")
# time.sleep(2)
#密码
inputs[1].send_keys("*")
# time.sleep(2)
button = browser.find_elements_by_class_name("button")
if len(button)==0:
    print("没有找到登陆按钮")
    browser.close()
button[0].click()



# 完成签到
#dom结构发生变化
#第一种dom
time.sleep(3)
button = browser.find_elements_by_xpath("/html/body/div[4]/div[6]/div[1]/div[3]/div[2]/div[1]/button")
# button[0].click()
if len(button)!=0:
    print("找到签到按钮")
    browser.execute_script("arguments[0].click();", button[0])
    time.sleep(10)
    button = browser.find_elements_by_xpath("/html/body/div[4]/div[6]/div[1]/div[3]/div[3]/div/div[3]")
    if len(button) != 0:
        print("找到签到确认领取按钮")
        button[0].click()
#第二种dom
time.sleep(3)
button = browser.find_elements_by_xpath("html/body/div[4]/div[7]/div[1]/div[3]/div[2]/div[1]/button")
if len(button)!=0:
    print("找到签到按钮")
    browser.execute_script("arguments[0].click();", button[0])
    time.sleep(10)
    button = browser.find_elements_by_xpath("/html/body/div[4]/div[6]/div[1]/div[3]/div[3]/div/div[3]")
    if len(button) != 0:
        print("找到签到确认领取按钮")
        button[0].click()
# 领取任务
button = browser.find_elements_by_xpath("/html/body/div[4]/div[6]/div[1]/div[4]/div[3]/div/div[2]/button/span")
if len(button) != 0:
    print("找到领取任务按钮")
    button[0].click()
    time.sleep(1)
    #寻找领取新任务按钮
    #切换到iframe
    browser.switch_to.frame("doingMession")

    button = browser.find_elements_by_class_name("messionApply")
    print(button)
    if len(button) != 0:
        print("找到了领取任务每日按钮")
        button[0].click()
time.sleep(1)
print("开始任务")
#切换回当前文档
browser.switch_to.default_content()
#发帖方法
def fatie(title,content):
    browser.get(url='https://club.geely.com/personalCenter/personalProfile')
    # 开始点击发帖任务
    button = browser.find_elements_by_id("fastPost")
    print(button)
    if len(button) != 0:
        print("到快速发帖按钮")
        button[0].click()
    # 开始编写帖子
    select = browser.find_elements_by_id("firstSelect")
    if len(select) != 0:
        print("已点击第一个选择框")
        select[0].click()
        # 选择官方圈子
        time.sleep(1)
        option = browser.find_elements_by_id("chouseGuanfang")
        option[0].click()
        # 选择车系
        time.sleep(1)
        select = browser.find_elements_by_id("forumSelect")
        select[0].click()
        # 选择缤越
        time.sleep(1)
        option = browser.find_elements_by_xpath(
            "/html/body/div[11]/form/div/div/div[2]/div[1]/div/div/select[3]/option[6]")
        option[0].click()
        # 输入标题
        time.sleep(1)
        input = browser.find_elements_by_id("subject")
        input[0].send_keys(title)
        # 输入内容
        # 切换到iframe
        time.sleep(1)
        browser.switch_to.frame("e_iframe")
        browser.find_element_by_tag_name('body').send_keys(content)
        # 切换到当前文档
        browser.switch_to.default_content()
        # 选择图片
        time.sleep(1)
        button = browser.find_elements_by_class_name("online-btn")
        button[0].click()
        # 选中图片
        time.sleep(3)
        button = browser.find_elements_by_class_name("img-block")
        button[0].click()
        time.sleep(1)
        button = browser.find_elements_by_class_name("online-chouse-btn")
        button[0].click()
        # 发表帖子
        time.sleep(1)
        button = browser.find_elements_by_id("postsubmit")
        button[0].click()
    time.sleep(10)
#评论方法

#发帖3次
title = "三缸优势。。"
content = "三缸发动机的优点是重量轻，体积小，燃油消耗量更低，尾气排放量也是更低的。三缸发动机要比四缸发动机少一个汽缸，少一个火花塞，少一个点火线圈，少一个进气歧管，少一个排气歧管，少一个喷油嘴，这样可以大大降低发动机的重量。三缸发动机的体积也是比较小的，这种发动机可以做的很紧凑。"
fatie(title,content)
title = "自适应巡航。。"
content = "自适应巡航控制系统是一种智能化的自动控制系统，它是在早已存在的巡航控制技术的基础上发展而来的。在车辆行驶过程中，安装在车辆前部的车距传感器（雷达）持续扫描车辆前方道路，同时轮速传感器采集车速信号。当与前车之间的距离过小时，ACC控制单元可以通过与制动防抱死系统、发动机控制系统协调动作，使车轮适当制动，并使发动机的输出功率下降，以使车辆与前方车辆始终保持安全距离。。。"
fatie(title,content)
title = "天窗保养。。"
content = "天窗的保养方法，有以下几种，可供参考:1、天窗使用一段时间后，会在滑轨还有缝隙中，沉积不少灰尘，若不定期清理，会损伤天窗的部件。一般天窗在使用两三个月之后，应该清理，用纱布沾着清水，稍微清洗一下，擦干后，可以放一点，润滑油。切记，千万不要抹机油或者是黄油，因为这两种油的黏度比较大，会沾上很多东西。2、对于电动天窗来说在，颠簸的路上，最好不要完全打开，因为可能会导致天窗与电机之间的振动而引起，一些部件变形，再严重的可能会损害电机。3、洗车后，天窗玻璃与密封胶框，可能会被冻着，此时你用蛮力打开的话，可能会损害天窗的电机，以及它的橡胶密封条。建议在洗车后，应该立刻将天窗打开，擦干边缘的水分，这样才有可能避免天窗被冻。因此，天窗的实用性也是非常的耐用，各位车主注意天窗的养护，这样可以延长它的使用寿命。"
fatie(title,content)









# button = browser.find_elements_by_class("contentlist")
# button[0].click()
# button = browser.find_element_by_css_selector('#su')
# button.click()
# browser.close()#关闭浏览器

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
