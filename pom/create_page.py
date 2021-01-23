"""
创建话题页面
"""
from pom.base_page import BasePage
class CreatePage(BasePage):

    def ceate_topic(self,tab,title,content):
        """
        发布话题
        :param tab: 选择版块
        :param title: 输入标题
        :param content: 输入内容
        :return:
        """