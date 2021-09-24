import math

m, n, r = input().split()
m, n, r = int(m), int(n), float(r)
ax, ay, bx, by = map(int, input().split())

# get to the same level
dist = abs(ay - by) * (r / n)

# the angle between them, distance from center to the closest one
theta = abs(ax - bx) * (math.pi / m)
radius = min(ay, by) * (r / n)

# arg length is angle times radius
dist += theta * radius

print(min(dist, ay*(r/n) + by*(r/n)))