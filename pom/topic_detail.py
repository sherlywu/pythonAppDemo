"""
话题详情页
"""
from pom.base_page import BasePage
class TopicDetail(BasePage):

    def reply_topic(self, content):
        """
        评论话题
        :param content: 输入评论
        :return:
        """
        # 点击评论按钮
        self.driver.find_element_by_id('org.cnodejs.android.md:id/fab_reply').click()
        # 输入评论内容
        reply_id = 'org.cnodejs.android.md:id/edt_content'
        self.driver.find_element_by_id(reply_id).click()
        self.driver.find_element_by_id(reply_id).send_keys(content)
        # 点击发送按钮
        self.driver.find_element_by_id('org.cnodejs.android.md:id/btn_tool_send').click()

        # 点击返回按钮回到首页
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@index="0"]').click()

    def up_topic(self):
        """
        给话题点赞
        :return:
        """
        # 切换到webview中
        # 1、先获取到所有元素
        contexts = self.driver.contexts
        print(contexts)
        # # 2、切换到webview页面
        # self.driver.switch_to.context(contexts[-1])
        # # 3.使用web方式点赞
        # up_xpath = '//td[@class="right1"]/img[@class="icon-button"]'
        # self.driver.find_element_by_xpath(up_xpath).click()
        # # 如果要切换原生应用，需要再切换出来
        # self.driver.switch_to.context(contexts[0])
        self.driver.find_element_by_xpath('//android.view.View[@index="10"]/android.widget.Image').click()
        # 点击返回按钮回到首页
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@index="0"]').click()