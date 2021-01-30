"""
用户相关
"""
from pom.main_page import MainPage
from pom.toggle_page import TogglePage
from pom.create_page import CreatePage

class TestUser:

    def test_login(self):
        """
        登录功能测试
        :return:
        """

    def test_score(self):
        """
        积分功能测试
        :return:
        """

    def test_logout(self):
        """
        注销功能测试
        :return:
        """

class TestScore:
    """
    主要测试积分功能
    """

    def test_score_display(self):
        """
        测试积分功能能够正常显示
        :return:
        """
        # 打开首页
        mainpage = MainPage()
        mainpage.click_toggle_btn()  # 点击左侧边栏弹出框

        # 左边栏框
        togglepage = TogglePage()
        text = togglepage.get_score()
        print('text', text)
        # 积分大于等于0
        assert int(text[3:]) >= 0

        # 将弹出框关闭
        togglepage.right_swipe()

    def test_score_auto_increament(self):
        """
        测试积分功能能够发布一个话题之后累加
        :return:
        """
        mainpage = MainPage()
        # 点击创建话题
        mainpage.click_create_topic_btn()

        # 创建话题
        createpage = CreatePage()
        createpage.ceate_topic(title='这是app自动化测试', tab='分享', content='使用pytest框架做app自动化测试')

        # 点击返回按钮 到首页
        createpage.driver.back()

        mainpage.click_toggle_btn()
        togglepage = TogglePage()
        newscore = togglepage.get_score()

        print("新积分:", newscore)
