year = int(input('what year is it? '))
day_count = 0
def days(year):
    year_check1 = year % 4
    year_check2 = year % 400
    if year_check1 == 0 and year_check2 == 0:
        day_count = 366
        print('the days in the year are',day_count,' days in a year')
    elif year_check1 != 0 or year_check2 == 0:
        day_count = 365
        print('the days in the year are ',day_count,' days in a year')
    return day_count
days(year)
