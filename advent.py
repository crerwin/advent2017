import argparse
from advent2017 import calendar

parser = argparse.ArgumentParser(description='adventofcode.com 2017 calendar')

parser.add_argument("day", type=int, 
    help="Specify which day to run")
parser.add_argument("part", type=int, 
    help="Specify which part of the specified day to run")

args = parser.parse_args()

print(calendar.dispatch(args.day, args.part))