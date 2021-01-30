"""
主页弹出的左边栏页面
"""

from pom.base_page import BasePage

class TogglePage(BasePage):

    def click_login_btn(self):
        # 点击头像登录
        self.driver.find_element_by_id('org.cnodejs.android.md:id/tv_login_name').click()

    def click_nav_by_customer_text(self, text):
        # 根据文本内容点击导航栏
        xpath = f'//android.widget.TextView[@resource-id="org.cnodejs.android.md:id/tv_title" and @text="{text}"]'
        self.driver.find_element_by_xpath(xpath).click()

    def get_score(self):
        """
        获取积分
        :return:
        """
        score_ele = self.driver.find_element_by_id('org.cnodejs.android.md:id/tv_score')
        return score_ele.text