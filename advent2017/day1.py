from .day import Day
from advent2017.input import load

class Day1(Day):
    def __init__(self):
        self.input_data = load.get_input(1)
    def part1(self):
        return process_captcha(self.input_data)

    def part2(self):
        return process_captcha_2(self.input_data)

def process_captcha(captcha):
    sum = 0
    for i in range(len(captcha)):
        if i == len(captcha) - 1:
            next = 0
        else:
            next = i + 1
        if captcha[i] == captcha[next]:
            sum += int(captcha[i])
    return sum

def process_captcha_2(captcha):
    sum = 0
    for i in range(len(captcha)):
        if i >= len(captcha)/2:
            compare = i - int(len(captcha)/2)
        else:
            compare = i + int(len(captcha)/2)
        if captcha[i] == captcha[compare]:
            sum += int(captcha[i])
    return sum