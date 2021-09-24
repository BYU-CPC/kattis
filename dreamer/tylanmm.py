from itertools import permutations

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return True

def solve(nums):
    dates = set()
    early = '99999999'
    for date in permutations(nums):
        date = ''.join(date)
        y, m, d = int(date[:4]), int(date[4:6]), int(date[6:])
        if y < 2000:
            continue
        if m == 0 or m > 12:
            continue
        days[2] = 29 if isLeapYear(y) else 28
        if d == 0 or d > days[m]:
            continue
        dates.add(date)
        early = min(early, date)
    return dates, early

for _ in range(int(input())):
    d, m, y = input().split()
    nums = list(d) + list(m) + list(y)
    dates, date = solve(nums)
    if dates:
        print(f'{len(dates)} {date[6:]} {date[4:6]} {date[:4]}')
    else:
        print(0)