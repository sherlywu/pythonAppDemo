"""
主页弹出的左边栏页面
"""

from pom.base_page import BasePage

class TogglePage(BasePage):

    def click_login_btn(self):
        # 点击头像登录
        self.driver.find_element_by_id('org.cnodejs.android.md:id/tv_login_name').click()