'''
mark
1.skip:在执行用例时，跳过有skip标记的用例，待修复之后在执行
2.自定义标记：
'''
import pytest

def test_case001():
    print("测试用例1")
@pytest.mark.skip(reason = "error")
def test_case002():
    print("测试用例2")

# 放到类上面，对类里面的每个方法生效
@pytest.mark.api
class TestUserMark:
    @pytest.mark.maoyan
    def test_case003(self):
        print("测试用例3")
    def test_case004(self):
        print("测试用例4")
    def test_case(self):
        print("测试用例5")


