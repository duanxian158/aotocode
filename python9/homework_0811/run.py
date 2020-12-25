#执行用例
import unittest
import HTMLTestRunner
from homework_0811.read_data import ReadData
from homework_0811.math_method import TestMath
test_data=ReadData().read_data()
if __name__ == '__main__':
    suite=unittest.TestSuite()
    print(test_data)

    for item in test_data:
        item=eval(item)
        print(item['a'],item['b'],item['expected'])
        suite.addTest(TestMath('test_add',item['a'],item['b'],item['expected']))
    with open('test_repot.html','wb+') as file:
        runner=HTMLTestRunner.HTMLTestRunner(file,title='python第9期')
        runner.run(suite)


