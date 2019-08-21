import importlib
from .day import Day

def dispatch(day, part):
    try:
        DayClass = getattr(importlib.import_module("advent2017.day" + str(day)), 
            "Day" + str(day))
        myday = DayClass()
    except:
        myday = Day()
    return myday.part(part)