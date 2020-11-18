'''
pytest的命名规则：
1.test_开头或者结尾的为测试文件
2.测试类为Test开头
3.测试方法以tset_开头

'''
import requests
import pytest

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data = data)
    return r


#手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone": "137123456789", "pwd": "123456pbc", "regname": "aaa"}
    # 预期结果
    expect = {"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}
    # 测试步骤
    real = register(data)
    # 结果校验
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]


def test_register_002():
    # 测试数据
    data = {"pwd": "123456abc", "regname": "aaa"}
    # 预期结果
    expect = {"status":0,"code":"20103","data":None,"msg":"手机号不能为空"}
    # 测试步骤
    real = register(data)
    # 结果校验
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]




def test_register_003():
    # 测试数据
    data = {"mobilephone":"13745241111","pwd":"123456abc","regname":"aaa"}
    # 预期结果
    expect = {"status":0,"code":"20110","data":None,"msg":"手机号码已被注册"}
    # 测试步骤
    real = register(data)
    # 结果校验
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]



def test_register_004():
    # 测试数据
    data = {"mobilephone":"13745241112","pwd":"12345678901234567890","regname":"aaa"}
    # 预期结果
    expect = {"status":"0","code":"20108","data":None,"msg":"密码长度必须为6~18"}
    # 测试步骤
    real = register(data)
    # 结果校验
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]
    assert real.json()["status"] == int(expect['status'])


def test_register_005():
    # 测试数据
    data = {"mobilephone":"13745241121","pwd":"12345678","regname":"Nasa"}
    # 预期结果
    expect = {"status":"1","code":"10001","msg":"注册成功"}
    # 测试步骤
    real = register(data)
    # 结果校验
    assert real.json()["msg"] == expect["msg"]
    assert real.json()["code"] == expect["code"]
    assert real.json()["status"] == int(expect['status'])



'''if __name__ == '__main__':

    pytest.main([-v","test_resgister.py"])
 '''