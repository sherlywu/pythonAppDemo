import pytest
import os
import time
from pom.base_page import BasePage

basepage = BasePage()

@pytest.fixture(scope='function', autouse=True)
def function_run():
    print('每个用例执行之前的操作')
    yield
    # print('每个用例执行之后的操作')
    # 定义每个用例运行完成之后进行截图操作
    # 1、设置截图目录
    screetshots = os.path.join(os.path.dirname(__file__), 'screenshots')
    # 2、创建截图目录
    if not os.path.exists(screetshots):
        os.mkdir(screetshots)
    # 3、设置截图文件名
    filename = time.strftime('%Y_%m_%d_%H_%M_%S')
    # 4、设置文件路径
    filepath = os.path.join(screetshots, filename+'.png')
    # 5、截图操作
    basepage.driver.save_screenshot(filepath)

@pytest.fixture(scope='class', autouse=True)
def class_run():
    print('整个class执行之前的操作')
    yield
    print('整个class执行之后的操作')

@pytest.fixture(scope='module', autouse=True)
def module_run():
    print('整个py文件执行之前的操作')
    yield
    print('整个py文件执行之后的操作')

@pytest.fixture(scope='session', autouse=True)
def session_run():
    print('所有的用例执行之前的操作')
    yield
    # print('所有的用例执行之后的操作')
    basepage.driver.quit()