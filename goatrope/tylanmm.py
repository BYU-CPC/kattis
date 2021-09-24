from math import sqrt
x, y, x1, y1, x2, y2 = map(int, input().split())
if x1 <= x <= x2:
    print(min(abs(y - y1), abs(y - y2)))
elif y1 <= y <= y2:
    print(min(abs(x - x1), abs(x - x2)))
elif x > x2 and y > y2:     # top right corner
    print(sqrt((x - x2)**2 + (y - y2)**2))
elif x > x2 and y < y1:     # bottom right corner
    print(sqrt((x - x2)**2 + (y - y1)**2))
elif x < x1 and y > y2:     # top left corner
    print(sqrt((x - x1)**2 + (y - y2)**2))
elif x < x1 and y < y1:     # bottom left corner
    print(sqrt((x - x1)**2 + (y - y1)**2))