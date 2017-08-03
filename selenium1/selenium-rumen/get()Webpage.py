import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 打开google浏览器
browser = webdriver.Chrome()
browser.get("http://www-alpha.mycloudhawk.com")
# 最大化浏览器
browser.maximize_window()
# 设置等待时间避免网页加载超时无法定位元素
time.sleep(2)
# 输入用户名
browser.find_element_by_class_name("username").send_keys("zhouyang@supeq.com")
# 输入密码
browser.find_element_by_css_selector(
    "body > my-app > main > login > div > form > div.control-group.h-45.mt-15 > input").send_keys("123456")
browser.find_element_by_css_selector("body > my-app > main > login > div > form > button").click()
time.sleep(5)
# 定位到setting元素的位置
setting = browser.find_element_by_xpath(
    "/html/body/my-app/main/pages/div/div[2]/site-header/header/site-nav/ul/li[6]/a")
# 鼠标移到元素的位置
ActionChains(browser).move_to_element(setting).perform()
# 点击poi按钮，使用标签的定位
browser.find_element_by_link_text("Point of interest").click()
time.sleep(2)
# 点击编辑按钮
browser.find_element_by_css_selector("body > my-app > main > pages > div > div:nth-child(3) > div > ng-component > "
                                     "ng-component > right-panel > div > div.content > ng-component > table > tbody > "
                                     "tr:nth-child(1) > td:nth-child(7) > i").click()
time.sleep(2)

# 定位到头像的元素位置
picture = browser.find_element_by_xpath("/html/body/my-app/main/pages/div/div["
                                        "2]/div/ng-component/ng-component/right-panel/div/div[1]/ng-component/form/div["
                                        "3]/image-crop-upload/div/img")
# 鼠标hover到元素的位置
ActionChains(browser).move_to_element(picture).perform()
time.sleep(2)
# 点击头像上的标签
browser.find_element_by_xpath("/html/body/my-app/main/pages/div/div["
                              "2]/div/ng-component/ng-component/right-panel/div/div[1]/ng-component/form/div["
                              "3]/image-crop-upload/div/i").click()
time.sleep(2)

# browser.find_element_by_xpath("/html/body/my-app/main/login/div/form/div[1]/input").send_keys("bbb")
# print(input_fist, input_second, input_third)
# print(input_third)
# browser.close()
