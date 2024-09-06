# how old am I in number of days?
# generalising
# what is 

def divisible_by(y,d):
    return y % d == 0

def is_leap_year(y):
    # a year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
    if divisible_by(y,4):
        if divisible_by(y,100):
            if divisible_by(y,400):
                return True
            return False
        return True
    else:
        return False
    
assert(is_leap_year(2024))
assert(not is_leap_year(2023))
assert(not is_leap_year(1700))
assert(not is_leap_year(1800))
assert(not is_leap_year(1900))
assert(is_leap_year(1600))
assert(is_leap_year(2000))


def days_in_year(y):
    # return the number of days in year y
    if is_leap_year(y):
        return 366
    else:
        return 365

def days_in_month(m,y):
    if m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    else:
        return 31

for m in range(1,13):
    print(days_in_month(m,2024))

def date_days(y1,m1,d1):
    # numbers of days since the epoch
    days = 0
    for y in range(1,y1):
        days = days + days_in_year(y)
    for m in range(1,m1):
        days = days + days_in_month(m,y1)
    days = days + m1
    return days
    
def date_diff(y1, m1, d1, y2, m2, d2):
    return date_days(y2,m2,d2) - date_days(y1,m1,d1)

def date_diff_approx(y1, m1, d1, y2, m2, d2):
    # returns the number of days between two arbitrary dates
    return (y2 - y1)*365.2422 + (m2 - m1) * 30.5 + (d2 - d1)

print(date_diff(1978,12,15, 2024,9,5))

