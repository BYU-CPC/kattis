from math import sin, cos, pi

for _ in range(int(input())):
    theta = 90
    x, y = 0, 0
    for i in range(int(input())):
        angle, d = map(float, input().split())
        theta += angle
        x += d * cos(theta * pi / 180)
        y += d * sin(theta * pi / 180)
    print(x, y)