import unittest
from class_0811_unittest.test_math_method import TestMathMethod
from class_0811_unittest  import test_math_method #具体到模块名
if __name__ == '__main__':
    test_data=[{'a':4,'b':5,'expected':9},{'a':-4,'b':-5,'expected':-9},{'a':0.2,'b':0.1,'expected':0.3}]
    # 2：收集所有用例--然后执行用例
    suite = unittest.TestSuite()  # 创建了一个测试套件，专门收集测试用例
    #suite必须在for循环后面
    for item in test_data:#遍历测试数据
        suite.addTests(TestMathMethod('test_data',item['a'],item['b'],item['expected']))

    #第一种方法：添加指定的用例
    # suite.addTest(TestMathMethod('test_add_two_positive'))
    # suite.addTest(TestMathMethod('test_add_two_negative'))
    # # suite.addTest(TestMathMethod('test_add_two_float'))
    # suite.addTest(TestMathMethod('test_add_one_arg'))

    #第二种方法 loader去加载用例 TestLoader
    loader=unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(test_math_method))
    #执行测试用例 TextTestRunner 专门执行测试用例的类
    file=open('test_result.txt','a+',encoding='UTF-8')
    # # 执行测试用例
    runner = unittest.TextTestRunner(stream=file,verbosity=2)
    runner.run(suite)

    #测试报告下节课再讲
    # file=open('test_report.html','wb+')
    # runner=HTMLTestRunnerNew.HTMLTestRunner(file,title='python期就是皮测试报告',description='哈哈，经于学会单元测试了',tester='星月')
    # runner.run(suite)