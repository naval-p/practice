'''
测试前置和后置
类和方法级别
'''

class Test002:
    def setup_calss(self):
        print("测试前置")

    def tearwown_class(self):
        print("测试后置")

    def setup_method(self):
        print("每个方法前执行")

    def teardown_method(self):
        print("每个方法后执行")


    def test_001(self):
        print("p")

    def test_002(self):
        print("w")


    def test_003(self):
        print("j")