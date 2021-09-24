n1, n2 = map(int, [input(), input()])
if n1 < n2:
    cw, ccw = n2 - n1, 360 - (n2 - n1)
else:
    cw, ccw = 360 - (n1 - n2), n1 - n2

if cw <= ccw:
    print(cw)
else:
    print(-ccw)