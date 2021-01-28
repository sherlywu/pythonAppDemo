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
        # 滑动操作
        windows_info = self.driver.get_window_rect()
        print(windows_info)
        # 滑动的起始点y轴
        start_y = windows_info['height'] / 4 * 3  # 3/4高度
        print('start_y:', start_y)
        # 滑动的结束点y轴
        end_y = windows_info['height'] / 4  # 1/4 高度
        print('end_y:',end_y)
        # 滑动的起始点和结束点的x轴（上滑操作x轴不变）
        x = windows_info['width'] / 2  # 1/2宽度
        for _ in range(10):
            # 向上滑动
            self.driver.swipe(start_x=x, start_y=start_y, end_x=x, end_y=end_y, duration=500)  # 单位 毫秒

    def swipe_down(self):
        """
        在主页下滑
        :return:
        """
        windows_info = self.driver.get_window_rect()
        print(windows_info)
        start_y = windows_info['height'] / 4  # 1/4高度
        end_y = windows_info['height'] / 4 * 3  # 3/4 高度
        x = windows_info['width'] / 2  # 1/2宽度
        for _ in range(10):
            # 向上滑动
            self.driver.swipe(start_x=x, start_y=start_y, end_x=x, end_y=end_y, duration=500)  # 单位 毫秒

    def click_create_topic_btn(self):
        """
        点击创建话题按钮
        :return:
        """
        topic_btn_id = 'org.cnodejs.android.md:id/fab_create_topic'
        self.driver.find_element_by_id(topic_btn_id).click()

    def select_topic(self, index):
        """
        选择某个话题
        :return:
        """
        xpath = f'//android.widget.LinearLayout[{index}]//android.widget.LinearLayout[@resource-id="org.cnodejs.android.md:id/btn_topic"]'
        self.driver.find_element_by_xpath(xpath).click()
        # self.driver.find_element_by_id('org.cnodejs.android.md:id/btn_topic').click()
