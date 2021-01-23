"""
主页页面
"""
import time
from pom.base_page import BasePage
class MainPage(BasePage):

    def click_toggle_btn(self):
        """
        点击抽屉栏按钮
        :return:
        """
        toggle_btn_xpath = '//android.view.ViewGroup[@resource-id="org.cnodejs.android.md:id/toolbar"]/android.widget.ImageButton'
        self.driver.find_element_by_xpath(toggle_btn_xpath).click()
        time.sleep(1)

    def swipe_up(self):
        """
        在主页上滑
        :return:
        """

    def click_create_topic_btn(self):
        """
        点击创建话题按钮
        :return:
        """