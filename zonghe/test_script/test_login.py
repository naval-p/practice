
import pytest
from zonghe.caw import DataRead
from zonghe.baw import Member, DbOp
import requests
#读取yaml文件
@pytest.fixture(params=DataRead.readyaml("zonghe/data_case/setup_data.yaml"))
def setup_data(request):
    return request.param

#登录的测试脚本（pytest)

@pytest.fixture(params=DataRead.readyaml("zonghe/data_case/login_pass.yaml"))
def pass_data(request):
    return request.param

#测试的前置和后置
@pytest.fixture()
def register(pass_data,url,baserequests,db):
    phone = pass_data['casedata']['mobilephone']
    DbOp.deleteUser(db,phone)
    Member.register(url,baserequests,pass_data['casedata'])
    yield
    #删除登录用户
    DbOp.deleteUser(db,phone)

#登录成功
def test_login_pass(register,pass_data,baserequests,url,db):

    #发送请求
    r = Member.login(url, baserequests, pass_data['casedata'])
    assert r.json()['code'] == pass_data['expect']['code']
    assert r.json()['msg'] == pass_data['expect']['msg']
