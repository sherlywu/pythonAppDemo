"""
数据驱动最基本的写法
"""
import pytest

@pytest.mark.skip(reason='demo练习')
@pytest.mark.parametrize("title, content", [("", "xxxxxxxxxxxx"), ("1234", ""), ("", ""), ("aaa", "aaa")])
def test_create_topic(title, content):
    print(f'开始测试，使用title:{title},content:{content}')