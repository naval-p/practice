'''
conftest.py:session级别的fixtrue放到这个文件中，名字一定时conftest

第一次调用这个fixtrue时执行前置，目录下所有文件执行完后执行后置
对同级目录以及子目录生效，一个工程中可以有多个conftest.py文件
'''
import pytest
@pytest.fixture(scope="session")
def login():
    print("login")
    yield
    print("exit")

