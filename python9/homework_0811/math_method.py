import unittest
from homework_0811 import math
class TestMath(unittest.TestCase):
    def __init__(self, methodName, a, b, expected):
        super(TestMath, self).__init__(methodName)#超继承
        self.a = a
        self.b = b
        self.expected = expected
    #测试用例
    def test_add(self):
        result=math.math().add(self.a,self.b)
        try:
            self.assertEqual(self.expected,result)
        except AssertionError as e:
            print('执行用例的时候出错了，报错是：')
            raise
        else:
            print('测试执行结果是：{0}'.format(result))