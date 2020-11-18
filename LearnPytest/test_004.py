'''
fixtrue:m默认为function级别，级别：有function，module，class，session级别
'''

import  pytest
@pytest.fixture(scope="class")#每个类调用一次，在类中首次调用fixtrue时执行前置，类方法执行完成后执行后置
def login():
    print("login")
    yield
    print("exit")


class TestQuery():
    def test_case1(self,login):
        print("测试查询1")

    def test_case2(self):
        print("测试查询2")

    def test_case3(self):
        print("测试查询3")


class TestDelete():
    def test_case1(self):
        print("测试删除1")

    def test_case2(self,login):
        print("测试删除2")

    def test_case3(self):
        print("测试删除3")