'''
fixtrue可以带参数和返回值

'''
#测试前置：准备测试数据，在测试用例中使用测试数据。测试数据使用fixture的返回值
import  pytest

@pytest.fixture()
def username_pwd():
    return {"username":"root","pwd":"123456"}#可以返回任意类型的数据

def test_login(username_pwd):
    print(f"测试数据为：{username_pwd['pwd']}")

@pytest.fixture(params=['root','admin','administrator','123456'])
def data(request):#固定写法
    return request.param#固定写法，取到每一组数据

@pytest.fixture(params=[
    {"testcase":'root',"expect":"成功"},
    {"testcase":'admin',"expect":"成功"}])
def data1(request):
    return request.param


@pytest.fixture(params=[
    {"testcase":'',"expect":"注册成功"},
    {"testcase":'18085086547',"expect":"注册成功"}])
def data2(request):
    return request.param

def test_login2(data):
    print(f"使用用户名：{data}测试登录功能")

def test_login3(data1):
    print(f"使用用户名：{data1['testcase']}测试登录功能，预期结果为{data1['expect']}")

def test_login4(data2):
    print(f"使用用户名：{data2['testcase']}测试注册功能，预期结果为{data2['expect']}")