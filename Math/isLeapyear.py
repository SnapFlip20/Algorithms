'''
return True for leap years, False for non-leap years.

윤년일 경우 1을, 아닐 경우 0을 반환합니다.
'''

# better
def isLeapyear(year):
    return ((year % 100 or year // 100) % 4) < 1


# normal
def isLeapyear2(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


# unique
def isLeapyear3(year):
    return (year % 400 == 0)^(year % 100 == 0)^(year % 4 == 0)


# using calendar module
import calendar

def isLeapyear4(year):
    if calendar.isleap(year):
        return True
    else:
        return False
'''
from calendar module......
def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
'''
