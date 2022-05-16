# -*- coding: UTF-8 -*-
"""
@Project ：PythonAutoTest 
@File    ：test_user.py
@IDE     ：PyCharm 
@Author  ：胖妞
@Date    ：2022/5/9 17:12
"""
import pytest


# def read_yaml():
#     return ['111', '222', '333']
#
#
# # #autouse自动执行，无需给方法传递参数
# @pytest.fixture(scope='function',autouse=True)
@pytest.fixture(scope='function', params=["user1", "user2", "user3"])
def my_fixture(request):
    print(request.param)
    print('执行sql语句')
    yield request.param
    print('关闭数据库连接')


class TestUser:
    age = 10

    def setup_class(self):
        print('每个类之前执行一次')

    def teardown_class(self):
        print('每个类之后执行一次')

    def setup(self):
        print('每个用例之前执行一次')

    def teardown(self):
        print('每个用例之后执行一次')

    # @pytest.mark.smoke
    def test_guoxiaorui(self):
        print('test guoxiaorui')

    @pytest.mark.skip(reason="无理由跳过")
    def test_a(self):
        print('test_a')

    @pytest.mark.skipif(age < 18, reason="年龄小于10，跳过")
    def test_b(self):
        print('test_b')

    def test_c(self):
        raise Exception('test_c error!!!')

    def test_d(self, my_fixture):
        print('test_d===' + my_fixture)
