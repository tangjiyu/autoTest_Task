from calculator import Count

import unittest

class TestSub(unittest.TestCase):
    def SetUp(self):
        print 'test case start'
    def SetDown(self):
        print 'test case end'
    def test_sub(self):
        j=Count(12,3)
        self.assertEqual(j.sub(),9)
    def test_sub2(self):
        j=Count(98,53)
        self.assertEqual(j.sub(),405)
if __name__ == '__main__':
    unittest.main()