import unittest
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
tests = unittest.defaultTestLoader.discover(r"E:\1234\study\day16\day16",pattern="Test*.py")
suite.addTests(tests)
f = open(file="银行系统测试报告.html",mode="w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title = "银行测试报告",
    verbosity = 2,
    description="执行用例的银行功能"
)
runner.run(suite)







