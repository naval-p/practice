'''
注册的测试脚本（pytest)
'''
import pytest
from zonghe.caw import DataRead
from zonghe.baw import Member, DbOp
import requests
#读取yaml文件
@pytest.fixture(params=DataRead.readyaml("zonghe/data_case/register_fail.yaml"))
def fail_data(request):
    return request.param

@pytest.fixture(params=DataRead.readyaml("zonghe/data_case/register_pass.yaml"))
def pass_data(request):
    return request.param

@pytest.fixture(params=DataRead.readyaml("zonghe/data_case/register_repeat.yaml"))
def repeat_data(request):
    return request.param


#注册失败
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为：{fail_data['expect']}")
    r = Member.register(url, baserequests,fail_data['casedata'])
    assert r.json()['code'] == fail_data['expect']['code']
    assert r.json()['msg'] == fail_data['expect']['msg']



#注册成功
def test_register_pass(pass_data,baserequests,url,db):
    print(f"测试数据为：{pass_data['casedata']}")
    print(f"预期结果为：{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']
    #初始化环境
    DbOp.deleteUser(db, phone)
    #发送请求
    r = Member.register(url, baserequests, pass_data['casedata'])
    assert r.json()['code'] == pass_data['expect']['code']
    assert r.json()['msg'] == pass_data['expect']['msg']

    #检查实际有没有注册成功
    r = Member.getList(url, baserequests)
    # print(r.text)
    assert phone in r.text


    #清理环境，根据手机号删除用户
    # DbOp.deleteUser(db,phone)



#重复注册
def test_register_repeat(repeat_data,baserequests,url):
    print(f"测试数据为：{repeat_data['casedata']}")
    print(f"预期结果为：{repeat_data['expect']}")
    r = Member.register(url, baserequests, repeat_data['casedata'])
    assert r.json()['code'] == repeat_data['expect']['code']
    assert r.json()['msg'] == repeat_data['expect']['msg']



