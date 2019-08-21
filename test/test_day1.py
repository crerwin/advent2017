import unittest
from advent2017 import day1

class captchaTestCase(unittest.TestCase):
    def testcaptcha(self):
        self.assertEqual(0, day1.process_captcha(""))
        self.assertEqual(3, day1.process_captcha("1122"))
        self.assertEqual(4, day1.process_captcha("1111"))
        self.assertEqual(0, day1.process_captcha("1234"))
        self.assertEqual(9, day1.process_captcha("91212129"))

    def testcaptcha2(self):
        self.assertEqual(0, day1.process_captcha_2(""))
        self.assertEqual(6, day1.process_captcha_2("1212"))
        self.assertEqual(0, day1.process_captcha_2("1221"))
        self.assertEqual(4, day1.process_captcha_2("123425"))
        self.assertEqual(12, day1.process_captcha_2("123123"))
        self.assertEqual(4, day1.process_captcha_2("12131415"))
