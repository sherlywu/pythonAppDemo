import time

from appium import webdriver
import os
from selenium.common.exceptions import NoSuchElementException

desired_caps = {
    'platformName': 'Android',  # 操作系统
    'platformVersion': '10',  # Android的版本
    'deviceName': '5ENDU19B01011350',  # adb devices 的设备串号值
    'automationName': 'UiAutomator2',
    'appPackage': 'com.sina.weibo',  # 指定启动的包名
    'appActivity': '.SplashActivity',  # 指定启动的app 启动页名称
    'noReset': True,  # 不要重置状态
    'fullReset': False,  # 重置所有的状态和数据，  False 为不要重置

}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 设置全局的隐式等待
driver.implicitly_wait(5)

for i in range(30):
    driver.swipe(start_x=100, start_y=800, end_x=100, end_y=400, duration=400)

    try:
        driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id="com.sina.weibo:id/rightButton"]').click()
    except NoSuchElementException:
        # 弹框
        eles = driver.find_elements_by_xpath('//android.webkit.WebView')
        if len(eles) == 0:   # 如果没有webview则继续滑动页面
            driver.swipe(start_x=100, start_y=1600, end_x=100, end_y=230, duration=400)
            continue
        os.system('adb shell input tap 145 580')
        # driver.find_element_by_xpath('//android.webkit.WebView//android.view.View[@index="3"]').click()
        time.sleep(2)

