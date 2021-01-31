from pom.main_page import MainPage
from pom.create_page import CreatePage
import pytest

@pytest.mark.order(3)
def test_create_topic():
    """
    编写发布话题测试用例
    :return:
    """
    # 实例化首页
    mainpage = MainPage()
    # 从首页点击发布话题按钮
    mainpage.click_create_topic_btn()

    # 实例化发布话题页面
    createpage = CreatePage()
    createpage.ceate_topic('分享', '这是app自动化测试标题', '这是app自动化测试代码发布的内容')

    # 发布成功的结果
    result_text = createpage.get_toast_text()

    # 添加断言
    assert result_text == '发布成功'

if __name__ == '__main__':
    pytest.main()