line = input()
while line != '0 0 0 0':
    s, a, b, c = map(int, line.split())
    amt = 720 + ((s - a) % 40)*9
    amt += 360 + ((b - a) % 40)*9
    amt += ((b - c) % 40)*9
    print(amt)
    line = input()   