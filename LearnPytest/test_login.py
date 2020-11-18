import pytest
import requests

@pytest.fixture(params=[{'testdata':{'mobilephone':'18586820522','pwd':'123456'},
                         'expectresult':{"status": 0, "code": "20111", "data": None, "msg": "用户名或密码错误"}},
                        {'testdata':{'mobilephone':'18586820531','pwd':'123456'},
                         'expectresult':{"status": 0, "code": "20111", "data": None, "msg": "用户名或密码错误"}},
                        {'testdata': {'mobilephone': '', 'pwd': '123456'},
                         'expectresult': {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}},
                        {'testdata': {'mobilephone': '18586820520', 'pwd': ''},
                         'expectresult': {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},
                        {'testdata': {'mobilephone': '15127345432', 'pwd': '123456'},
                         'expectresult': {"status": 1, "code": "10001", "data": None, "msg": "登录成功"}}])

def login(request):
    return request.param

def test_login(login):
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    r = requests.post(url,data = login['testdata'])
    assert r.json()['code'] == login['expectresult']['code']
    assert r.json()['msg'] == login['expectresult']['msg']