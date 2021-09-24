from math import cos, radians

def vf(vi, a, d):
    return (vi**2 + 2*a*d)**0.5

n, g = map(float, input().split())
n = int(n)
segs = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    v = 0
    for j in range(i, n):
        v = vf(v, g*cos(radians(segs[j][1])), segs[j][0])
    print(v)