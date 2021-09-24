from sys import stdin
from math import pi, acos

for line in stdin.readlines():
    r, x, y = map(float, line.split())
    dist = (x*x + y*y)**0.5
    if dist >= r:
        print('miss')
        continue
    
    circle = pi * r**2
    sector = acos(dist / r) * r**2
    # dist is the height, Pythagorean theorem to find base
    # don't need to * 1/2 because we're only getting half the chord length
    tri = dist * (r*r - dist**2)**0.5
    p1 = sector - tri
    p2 = circle - p1
    print(max(p1, p2), min(p1, p2))
