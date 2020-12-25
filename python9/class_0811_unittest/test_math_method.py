
import unittest #引入Python的单元测试模块

from class_0811_unittest.math_method import MathMethod

#针对加法 你会想到哪些测试点？ 开始写测试用例
#类型  参数的个数 大小
#1：输入两个正数
#2：输入2个负数
#3：输入2个小数
#4：只输入一个参数
#TestCase 专门来写测试用例的 我们会把测试用例组织在测试类里面
#用例是作为测试类一个个的函数
class TestMathMethod(unittest.TestCase):
    def __init__(self,methodName,a,b,expected):
        super(TestMathMethod,self).__init__(methodName)
        self.a=a
        self.b=b
        self.expected=expected
    def setUp(self):#在测试用例执行之前做一些准备工作
        print('hello start')
    def test_add(self):
        result=MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(self.expected,result)
        except AssertionError as e:
            print('执行用例的时候出错了，报错是：')
            raise
        else:
            print('测试执行结果是：{0}'.format(result))
    #写用例 test_ 前缀 以这个开头
    # def test_add_two_positive(self):#1：输入两个正数
    #     result=MathMethod().add(4,5)
    #     try:
    #         self.assertEquals(9,result) #断言 比较期望值和实际值
    #     except AssertionError as e:
    #         print('执行用例出错了{0}'.format(e))
    #     print('我正在执行加法运算，结果是{0}'.format(result))
    # def test_add_two_negative(self):#1：输入两个负数
    #     result=MathMethod().add(-4,-5)
    #     self.assertEquals(-9,result)
    #     print('我正在执行加法运算，结果是{0}'.format(result))
    # def test_add_two_float(self):#3：输入2个小数
    #     result = MathMethod().add(-0.2,-0.1)
    #     #result=round(result,1)
    #     try:
    #         self.assertEquals(-0.3,result)
    #     except AssertionError as e:
    #         print('执行用例出错了{0}'.format(e))
    #         raise e #抛出错误？
    #     print('我正在执行加法运算，结果是{0}'.format(result))
    # def test_add_one_arg(self):#4：只输入一个参数
    #     result = MathMethod().add(1)
    #     self.assertEquals(None,result)
    #     print('我正在执行加法运算，结果是{0}'.format(result))
    def tearDown(self):
        print('hello finish')
#2：收集所有用例--然后执行用例
# suite=unittest.TestSuite()#创建了一个测试套件，专门收集测试用例
# suite.addTest(TestMathMethod('test_add_two_positive'))
# suite.addTest(TestMathMethod('test_add_two_negative'))
# suite.addTest(TestMathMethod('test_add_two_float'))
# suite.addTest(TestMathMethod('test_add_one_arg'))
# #执行测试用例
# runner=unittest.TextTestRunner()
# runner.run(suite)