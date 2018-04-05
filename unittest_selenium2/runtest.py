import unittest
import testadd
import testsub

suite=unittest.TestSuite()
suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testsub.TestSub("test_sub"))
suite.addTest(testsub.TestSub("test_sub2"))

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)
    