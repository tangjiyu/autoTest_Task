from calculator import Count

import unittest

class TestAdd(unittest.TestCase):
    def SetUp(self):
        print 'test case start'
    def SetDown(self):
        print 'test case end'
    def test_add(self):
        j=Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j=Count(12,53)
        self.assertEqual(j.add(),65)
if __name__ == '__main__':
    unittest.main()