import pytest

from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests

#从环境文件中读取url
@pytest.fixture(scope='session')
def url():
    return DataRead.readini("zonghe/data_env/env.ini","url")

#从环境文件中读取db
@pytest.fixture(scope='session')
def db():
    #使用eval（），将字符串转为字典
    return eval(DataRead.readini("zonghe/data_env/env.ini","db"))


#创建一个requests的实例
@pytest.fixture(scope="session")
def baserequests():
    return BaseRequests()