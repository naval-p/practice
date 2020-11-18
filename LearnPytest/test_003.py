'''比较灵活的前置和后置、
1.不受setup，teardown的命名限制
2.使用更加灵活

'''
import pytest

#测试前置,使用foxture来修饰
@pytest.fixture(scope = 'module')#作用域：module级别的，首次调用这个fixtrue的地方执行前置，所有用例执行完后在执行后置
def login():
    print("系统登录")
    #yield之前为前置，之后为后置
    yield
    print("退出系统")

@pytest.fixture(autouse=True)
def db_op():
    print("；连接数据库")
    yield
    print("断开数据库连接")

#将测试前置作为参数传进来
def test_001(login):
    print("用例1：查询操作，不需要绑定")

@pytest.mark.usefixtures('login')
def test_002():
    print("用例2：添加操作，需要登录")

def test_003(login):
    print("用例3：删除操作，需要登录")

def test_004():
    print("用例4：")