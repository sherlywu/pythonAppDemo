from pom.main_page import MainPage
from pom.login_page import LoginPage
from pom.toggle_page import TogglePage
from pom.create_page import CreatePage
from pom.topic_detail import TopicDetail

if __name__ == '__main__':
    mainpage = MainPage()
    # 点击抽屉按钮
    mainpage.click_toggle_btn()
    togglepage = TogglePage()
    # 点击头像登录
    togglepage.click_login_btn()
    # 用户登录
    loginpage = LoginPage()
    loginpage.login_with_token('f65f4ec8-a807-416a-a2fc-a0eb9ddc5db1')
    text = loginpage.get_login_status()
    print('text:', text)
    # togglepage.click_nav_by_customer_text('精华')
    #
    # mainpage.click_toggle_btn()
    # togglepage.click_nav_by_customer_text('分享')
    #
    # mainpage.click_toggle_btn()
    # togglepage.click_nav_by_customer_text('问答')

    # 点击1次发布话题按钮关闭抽屉
    mainpage.click_create_topic_btn()
    # 点击发布话题进入创建话题页
    # mainpage.click_create_topic_btn()

    # 发布话题
    # createpage = CreatePage()
    # createpage.ceate_topic('问答', '这是app自动化测试标题', '这是app自动化测试代码发布的内容')

    # 选择话题
    # mainpage.select_topic(3)
    # 评论话题
    # topicdetail = TopicDetail()
    # topicdetail.reply_topic('这是app自动化测试代码自动回复的评论哦~')

    # 选择话题
    topicdetail = TopicDetail()
    mainpage.select_topic(1)
    # 点赞评论
    topicdetail.up_topic()