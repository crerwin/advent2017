import unittest
from advent2017 import day2

class checksumTestCase(unittest.TestCase):
    def test_row_to_ints(self):
        self.assertEqual([5, 1, 9, 5], 
            day2.row_to_ints("5 1 9 5"))

    def test_checksum_row(self):
        self.assertEqual(8, day2.checksum_row([5, 1, 9, 5]))
        self.assertEqual(4, day2.checksum_row([7, 5, 3]))
        self.assertEqual(6, day2.checksum_row([2, 4, 6, 8]))

    def test_checksum_row2(self):
        self.assertEqual(4, day2.checksum_row2([5, 9, 2, 8]))
        self.assertEqual(3, day2.checksum_row2([9, 4, 7, 3]))
        self.assertEqual(2, day2.checksum_row2([3, 8, 6, 5]))

    def test_checksum(self):
        input = '''5 1 9 5
7 5 3
2 4 6 8'''
        self.assertEqual(18, day2.checksum(input))

    def test_checksum2(self):
        input = '''
5 9 2 8
9 4 7 3
3 8 6 5
'''
        self.assertEqual(9, day2.checksum2(input))