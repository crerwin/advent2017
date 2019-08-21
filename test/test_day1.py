from advent2017 import day1

def test_captcha():
    assert day1.process_captcha("") == 0
    assert day1.process_captcha("1122") == 3
    assert day1.process_captcha("1111") == 4
    assert day1.process_captcha("1234") == 0
    assert day1.process_captcha("91212129") == 9

def test_captcha2():
    assert day1.process_captcha_2("") == 0
    assert day1.process_captcha_2("1212") == 6
    assert day1.process_captcha_2("1221") == 0
    assert day1.process_captcha_2("123425") == 4
    assert day1.process_captcha_2("123123") == 12
    assert day1.process_captcha_2("12131415") == 4
