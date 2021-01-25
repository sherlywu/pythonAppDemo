"""
话题详情页
"""
import time

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

    def up_topic(self, index):
        """
        给话题点赞
        :return: index：第几个位置的点赞
        """
        # 1、先获取到所有元素
        contexts = self.driver.contexts
        print(contexts)
        # 2、切换到webview 中
        self.driver.switch_to.context(contexts[-1])
        # 3、使用web方式点赞
        ele_text = self.driver.find_element_by_xpath('//div[@class="reply-count text-primary"]').text
        print(ele_text)
        if '回复' in ele_text:
            up_xpath = f'//div[@class="cell"][{index}]//td[@class="right1"]'
            name_xpath = f'//div[@class="cell"][{index}]//span[@class="loginname text-primary"]'
            name_text = self.driver.find_element_by_xpath(name_xpath).text
            print(name_text)
            if name_text != 'fanmao59':
                self.driver.find_element_by_xpath(up_xpath).click()
            else:
                print('无法给自己的评论点赞')
        # 如果要切换原生应用，需要再切换出来
        self.driver.switch_to.context(contexts[0])
        # 点击返回按钮回到首页
        self.driver.find_element_by_xpath('//android.widget.ImageButton[@index="0"]').click()