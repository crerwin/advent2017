from advent2017 import day 

def test_init():
    test_day = day.Day()
    assert test_day.input_data == ""

def test_part():
    test_day = day.Day()
    assert test_day.part(1) == "not yet implemented"
    assert test_day.part(2) == "not yet implemented"
    assert test_day.part(3) == "invalid part number specified - only 1 and 2 are valid."
    assert test_day.part(0) == "invalid part number specified - only 1 and 2 are valid."
    assert test_day.part(-1) == "invalid part number specified - only 1 and 2 are valid."
    assert test_day.part(3.14) == "invalid part number specified - only 1 and 2 are valid."
    assert test_day.part("a string") == "invalid part number specified - only 1 and 2 are valid."

def test_part1():
    test_day = day.Day()
    assert test_day.part1() == "not yet implemented"

def test_part2():
    test_day = day.Day()
    assert test_day.part2() == "not yet implemented"