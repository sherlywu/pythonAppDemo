import time

from pom.base_page import BasePage

class ReplyPage(BasePage):

    def reply(self, content):
        """
        回复话题
        :return:
        """
        # 点击评论按钮
        self.driver.find_element_by_id('org.cnodejs.android.md:id/fab_reply').click()
        # 输入评论内容
        edit_content = self.driver.find_element_by_id('org.cnodejs.android.md:id/edt_content')
        edit_content.clear()
        edit_content.send_keys(content)

        # 点击发布按钮
        self.driver.find_element_by_id('org.cnodejs.android.md:id/btn_tool_send').click()
        time.sleep(2)

    def click_up(self, index):
        # # 获取所有的contexts
        # allcontexts = self.driver.contexts
        # print(allcontexts)
        # # 切换到webview中
        # self.driver.switch_to.context(allcontexts[-1])
        # # 点赞
        # up_xpath = f'//div[@class="cell"][{index}]//td[@class="right1"]'
        # self.driver.find_element_by_xpath(up_xpath).click()
        # print('点赞了！')
        #
        # # 切换到原生中
        # self.driver.switch_to.context(allcontexts[0])
        """
        给话题点赞
        :return: index：第几个位置的点赞
        """
        contexts = self.driver.contexts
        print(contexts)
        # 2、切换到webview 中
        self.driver.switch_to.context(contexts[-1])
        time.sleep(2)
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
