import unittest
from advent2017 import day 

class dayTestCase(unittest.TestCase):
    def testInit(self):
        test_day = day.Day()
        self.assertEqual("", test_day.input_data)