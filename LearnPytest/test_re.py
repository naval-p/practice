import pytest
import requests

@pytest.fixture(params = [{'testdata':{'mobilephone':'18586820529','pwd':'123456','regname':'cxm'},'expectresult':{"status":0,"code":"20110","data":None,"msg":"手机号码已被注册"}},
                          {'testdata':{'mobilephone':'133','pwd':'123456','regname':'cxm'},'expectresult':{"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}},
                          {'testdata':{'mobilephone':'1333333333333333333333','pwd':'123456','regname':'cxm'},'expectresult':{"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}},
                          {'testdata': {'mobilephone':'13315016469','pwd':'12345','regname':'cxm'},'expectresult':{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}},
                          {'testdata': {'mobilephone':'13315016469','pwd':'1234511111111111111','regname':'cxm'},'expectresult':{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}},
                          {'testdata': {'mobilephone':'','pwd':'12345','regname':'cxm'},'expectresult':{"status":0,"code":"20103","data":None,"msg":"手机号不能为空"}},
                          {'testdata': {'mobilephone':'13315016469','pwd':'','regname':'cxm'},'expectresult':{"status":0,"code":"20103","data":None,"msg":"密码不能为空"}},
                          {'testdata': {'mobilephone':'13315016469','pwd':'123456','regname':''},'expectresult':{"status":0,"code":"20110","data":None,"msg":"手机号码已被注册"}},
                          {'testdata':{'mobilephone':'15127025433','pwd':'123456','regname':'cxm'},'expectresult':{"status":1,"code":"10001","data":None,"msg":"注册成功"}},
                          ])
def data(request):
    return request.param

def test_register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data=data['testdata'])
    assert r.json()['code'] == data['expectresult']['code']
    assert r.json()['msg'] == data['expectresult']['msg']
