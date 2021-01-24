"""
创建话题页面
"""
from pom.base_page import BasePage
class CreatePage(BasePage):

    def ceate_topic(self, tab, title, content):
        """
        发布话题
        :param tab: 选择版块
        :param title: 输入标题
        :param content: 输入内容
        :return:
        """
        # 点击发布到分类按钮
        self.driver.find_element_by_id('android:id/text1').click()
        # 点击分类方法
        tab_xpath = f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="{tab}" ]'
        self.driver.find_element_by_xpath(tab_xpath).click()
        # 输入title
        title_id = 'org.cnodejs.android.md:id/edt_title'
        self.driver.find_element_by_id(title_id).click()
        self.driver.find_element_by_id(title_id).send_keys(title)
        # 输入内容
        content_id = 'org.cnodejs.android.md:id/edt_content'
        self.driver.find_element_by_id(content_id).click()
        self.driver.find_element_by_id(content_id).send_keys(content)

        # 点击发布按钮
        self.driver.find_element_by_id('org.cnodejs.android.md:id/action_send').click()

        # 点击返回按钮回到首页
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@index="0"]').click()
