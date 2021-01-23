"""
登录页面
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from pom.base_page import BasePage
class LoginPage(BasePage):

    def login_with_token(self, token):
        """
        使用token方式进行登录
        :return:
        """
        self.driver.find_element_by_id('org.cnodejs.android.md:id/edt_access_token').send_keys(token)
        self.driver.find_element_by_id('org.cnodejs.android.md:id/btn_login').click()

    def get_login_status(self):
        """
        获取用户登录成功之后的Toast的信息
        :return:
        """
        # 根据Android开发文档中推测 组件名为     android.widget.Toast
        # 针对单个元素设置最长等待3秒时间
        # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Toast')))
        # ele = self.driver.find_element(By.XPATH, '//android.widget.Toast')
        ele = self.driver.find_element_by_xpath('//android.widget.Toast')
        # 返回文本值
        return ele.text