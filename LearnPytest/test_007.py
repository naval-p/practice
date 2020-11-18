'''
1.接口测试场景难以模拟，需要大量的工作才能完成
2.依赖第三方的接口，但是第三方的接口没有开发完成
3.测试环境不充分的情况下
使用mock来模拟
'''
from unittest import mock
import requests


class Alipay:
    def zhifu(self,data):
        #接口功能尚未开发完成
        #接口地址、get/post 入参。返回值已经定义好，有对应的接口
        #接口参数："orderid":"4588796","Amount":"200","Type":"支付宝"
        #接口返回值："code":200,"msg":"支付成功"

        r = requests.post("http://zhifubao.com/pay", data=data).json()
        return r

class TestMock:
    def test_alipay(self):
        #实例化一个模拟对象
        alipay = Alipay()
        #模拟支付的返回值
        # alipay.zhifu = mock.Mock(return_value={"code":200,"msg":"支付成功"})
        #调用支付接口
        data = {"orderid":"4588796","Amount":"200","Type":"支付宝"}
        w = alipay.zhifu(data)
        print(w)