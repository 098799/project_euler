month_table = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_table_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def how_many_sundays(start, year, result=0):
    if year % 4 == 0:
        months = month_table_leap
    else:
        months = month_table

    for month in months:
        start += month
        start = start % 7
        if start == 0:
            result += 1
    return start, year+1, result


starting_values = (2, 1901)
for year in range(1901, 2001):
    starting_values = how_many_sundays(*starting_values)

print(starting_values[-1])
