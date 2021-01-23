"""
登录页面
"""
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# 内置等待元素方法
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from pom.base_page import BasePage
class LoginPage(BasePage):

    def login_with_token(self,token):
        """
        使用token值的方式进行登录
        :return:
        """
        # 针对此元素设置最长等待时间为5s
        print('---------开始执行等待-----------')
        # self.driver.implicitly_wait(0)
        try:
            start_time = time.perf_counter()
            # 设置单个元素的最长等待时间为20s
            input_area = WebDriverWait(self.driver,20).until(presence_of_element_located((By.ID,'org.cnodejs.android.md:id/edt_access_token')))
        except TimeoutException:
            end_time = time.perf_counter()
            print(f'总共使用了时间：{end_time - start_time}s')
        print('----------执行等待结束------------------------')
        input_area.send_keys(token)
        # self.driver.find_element_by_id('org.cnodejs.android.md:id/edt_access_token').send_keys(token)
        self.driver.find_element_by_id('org.cnodejs.android.md:id/btn_login').click()

    def get_login_status(self):
        """
        获取用户登录成功之后的Toast的信息
        :return:
        """
        # 根据Android开发文档中推测 组件名为     android.widget.Toast
        ele = self.driver.find_element_by_xpath('//android.widget.Toast')
        # 返回文本值
        return ele.text