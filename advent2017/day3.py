import math
from .day import Day
from advent2017.input import load

class Day3(Day):
    def __init__(self):
        self.input_data = load.get_input(3)

    def part1(self):
        return find_retrieval_distance(self.input_data)

def manhattan_distance(location1, location2):
    x1, y1 = location1
    x2, y2 = location2
    return abs(x1 - x2) + abs(y1 - y2)

def find_position(number):
    if number == 1:
        return (0, 0)
    if number < 1:
        return (0, 0)
    x = 0
    y = 0
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    direction = "right"
    for n in range(number-1):
        if direction == "right":
            x += 1
            if x > max_x:
                max_x = x
                direction = "up"
        elif direction == "up":
            y += 1
            if y > max_y:
                max_y = y
                direction = "left"
        elif direction == "left":
            x -= 1
            if x < min_x:
                min_x = x
                direction = "down"
        elif direction == "down":
            y -= 1
            if y < min_y:
                min_y = y
                direction = "right"
        else:
            raise("invalid direction")
        


    return (x, y)

def find_retrieval_distance(number):
    position = find_position(number)
    return manhattan_distance(position, (0, 0))