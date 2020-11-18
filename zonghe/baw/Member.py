'''
用户模块的接口（注册、登录、充值、用户列表、取现
'''

def register(url,baserequests,data):
    '''

    :param url: http://jy0004:8081
    :param baserequests: 是Baserequests的一个实例
    :param data: 注册接口的参数
    :return: 相应信息
    '''
    url = url+"futureloan/mvc/api/member/register"
    r = baserequests.post(url,data = data)
    return r

def getList(url,baserequests):
    url = url+"futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r

def login(url,baserequests,data):
    url = url+"futureloan/mvc/api/member/login"
    r = baserequests.post(url,data=data)
    return r

'''
if __name__ == '__main__':
    from zonghe.caw.BaseRequests import BaseRequests
    baserequesters = BaseRequests()
    canshu = {"mobilephone":"123123123","pwd":"123"}
    r = register("http://jy001:8081/",baserequesters,canshu)
    print(r.json())
'''