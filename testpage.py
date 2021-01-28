from pom.main_page import MainPage
from pom.login_page import LoginPage
from pom.toggle_page import TogglePage
from pom.create_page import CreatePage
from pom.reply_page import ReplyPage

if __name__ == '__main__':
    # # 实例化首页，点击抽屉按钮
    mainpage = MainPage()
    # mainpage.click_toggle_btn()
    # # 实例化抽屉页，点击头像登录
    # togglepage = TogglePage()
    # togglepage.click_login_btn()
    # # 实例化登录页，完成登录，获取登录成功的toast提示
    # loginpage = LoginPage()
    # loginpage.login_with_token('f65f4ec8-a807-416a-a2fc-a0eb9ddc5db1')
    # text = loginpage.get_login_status()
    # print('text:', text)

    # 点击2次发布话题按钮关闭抽屉页，进入创建话题页
    # mainpage.click_create_topic_btn()
    # mainpage.click_create_topic_btn()

    # 发布话题
    # createpage = CreatePage()
    # createpage.ceate_topic('问答', '这是app自动化测试标题', '这是app自动化测试代码发布的内容')
    # mainpage.back_mainpage()
    # 选择话题
    mainpage.select_topic(1)
    # 回复话题
    reply = ReplyPage()
    # reply.reply('这是app自动化测试代码自动回复的评论哦~')
    # 给回复点赞
    reply.click_up(1)

    # 获取toast文本值
    # text = replypage.get_toast_text()
    # print('toast_text:', text)


