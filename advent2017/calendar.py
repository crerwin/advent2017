import importlib
from .day import Day

def dispatch(day, part):
    # Here we'll try to instantiate the given day.  If it hasn't been 
    # implemented yet, we'll get an exception and instead instantiate a generic
    # Day so that the not implemented yet message is returned to the user.
    try:
        DayClass = getattr(importlib.import_module("advent2017.day" + str(day)), 
            "Day" + str(day))
        myday = DayClass()
    except:
        myday = Day()
    return myday.part(part)