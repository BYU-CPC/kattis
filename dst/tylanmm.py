for _ in range(int(input())):
    dir, d, h, m = input().split()
    d, h, m = map(int, [d, h, m])
    if dir == 'F':
        m += d
        while m >= 60:
            m -= 60
            h += 1
        h %= 24
    else:
        m -= d
        while m < 0:
            m += 60
            h -= 1
        h %= 24
    print(h, m)