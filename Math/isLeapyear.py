# ----------------------------------------------------------------------- #
def isLeapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# ----------------------------------------------------------------------- #
def isLeapyear(year):
    return ((year % 100 or year // 100) % 4) < 1

# ----------------------------------------------------------------------- #
def isLeapyear(year):
    return (year % 400 == 0)^(year % 100 == 0)^(year % 4 == 0)

# ----------------------------------------------------------------------- #
from calendar import isLeapyear
def isLeapyear(year):
    return isLeapyear(year)

# ----------------------------------------------------------------------- #
def isLeapyear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# ----------------------------------------------------------------------- #
def f(y):return y%16*(y%25<1)<(y%4<1)