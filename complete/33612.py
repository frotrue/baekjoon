year = 2024
month = 1
a = int(input())

month += a*7
if month > 12:
    year += month//12
    month = month%12
    if month == 0:
        month = 12
        year -= 1
print(year, month)