'''
测试前置和后置

模块级（每个模块执行一次）和函数级（每个函数执行一次）一起用。


'''
def setup_module():
    print("测试前置：打开游戏")

def teardown_module():
    print("测试后置：退出游戏")

def setup_function():
    print("测试前置：开始录制")

def teardown_function():
    print("测试后置：录制结束")

def test_001():
    print("first blood")

def test_002():
    print("double kill")

def test_003():
    print("touble kill")

