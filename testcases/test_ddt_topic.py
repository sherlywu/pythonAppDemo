"""
使用数据驱动的方式进行发布话题的自动化测试
"""
import pytest
from pom.main_page import MainPage
from pom.create_page import CreatePage

testdata = [('', 'helloworld', '标题要求10字以上'),
            ('12345', 'helloworld', '标题要求10字以上'),
            ('1234567890', '', '内容不能为空'),
            ('12345', '', '标题要求10字以上'),
            ('', '', '标题要求10字以上')]

# 添加整个class之前的操作
@pytest.fixture(scope='class', autouse=True)
def beforeDDT():
    mainpage = MainPage()
    mainpage.click_create_topic_btn()

class TestDDT:
    @pytest.mark.parametrize("title,content,except_msg", testdata)
    def test_create_topic(self, title, content, except_msg):
        createpage = CreatePage()
        createpage.ceate_topic('分享', title, content)

        # 获取toast文本
        text = createpage.get_toast_text()
        # 断言文本值应该与期望结果一致
        assert text == except_msg