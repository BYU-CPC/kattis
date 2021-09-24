from math import cos, pi, sin

for _ in range(int(input())):
    v, theta, x, h1, h2 = map(float, input().split())
    t = x / (v * cos(pi / 180 * theta))
    y = v*t*sin(pi / 180 * theta) - 9.81*t*t/2
    if y + 1 < h2 and y - 1 > h1:
        print('Safe')
    else:
        print('Not Safe')