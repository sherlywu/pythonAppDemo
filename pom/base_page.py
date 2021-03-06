"""
所有页面模型的父类
所有页面都继承此类
在父类中提供所有子类的driver
"""
from appium import webdriver
import os

class BasePage:
    DRIVER = None
    def __init__(self):
        chromdriverpath = os.path.abspath(os.path.join(os.path.dirname(__file__), 'chromedriver'))
        desired_caps = {
            'platformName': 'Android',  # 操作系统
            'platformVersion': '10',  # Android的版本
            'deviceName': '5ENDU19B01011350',  # adb devices 的设备串号值
            'automationName': 'UiAutomator2',
            'appPackage': 'org.cnodejs.android.md',  # 指定启动的包名
            'appActivity': '.ui.activity.LaunchActivity',  # 指定启动的app 启动页名称
            'noReset': True,  # 不要重置状态
            'fullReset': False,  # 重置所有的状态和数据，  False 为不要重置
            'chromedriverExecutable': chromdriverpath,  # 配置chromedriver 的绝对路径。

        }
        # 当driver为空时，创建driver
        self.driver = BasePage.DRIVER
        if BasePage.DRIVER is None:
            # 创建driver
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        BasePage.DRIVER = self.driver
        # 设置全局的隐式等待
        self.driver.implicitly_wait(5)

    def get_toast_text(self):
        # 根据Android开发文档中推测 组件名为 	android.widget.Toast
        ele = self.driver.find_element_by_xpath('//android.widget.Toast')
        # 返回文本值
        return ele.text

    def right_swipe(self):
        rect = self.driver.get_window_rect()
        x = rect.get('width')
        y = rect.get('height')
        self.driver.swipe(start_x=x - 10, end_x=10, start_y=y / 2, end_y=y / 2, duration=400)

    def back_mainpage(self):
        back_xpath = '//android.view.ViewGroup[@resource-id="org.cnodejs.android.md:id/toolbar"]/android.widget.ImageButton'
        self.driver.find_element_by_xpath(back_xpath).click()



