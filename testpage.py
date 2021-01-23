from pom.main_page import MainPage
from pom.login_page import LoginPage
from pom.toggle_page import TogglePage

if __name__ == '__main__':
    mainpage = MainPage()
    # 点击抽屉按钮
    mainpage.click_toggle_btn()
    togglepage = TogglePage()
    # # 点击头像登录
    # togglepage.click_login_btn()
    # 用户登录
    # loginpage = LoginPage()
    # loginpage.login_with_token('f65f4ec8-a807-416a-a2fc-a0eb9ddc5db1')
    # text = loginpage.get_login_status()
    # print('text:', text)
    togglepage.click_nav_by_customer_text('精华')

    mainpage.click_toggle_btn()
    togglepage.click_nav_by_customer_text('分享')

    mainpage.click_toggle_btn()
    togglepage.click_nav_by_customer_text('问答')