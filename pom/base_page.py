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
            'platformVersion': '8.0.0',  # Android的版本
            'deviceName': 'ac35bdba',  # adb devices 的设备串号值
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
        self.driver.implicitly_wait(10)