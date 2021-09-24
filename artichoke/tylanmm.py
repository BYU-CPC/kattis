from math import sin, cos
p, a, b, c, d, n = map(int, input().split())

def price(k):
    return p * (sin(a*k + b) + cos(c*k + d) + 2)

hi = price(1)
best = 0
for i in range(2, n+1):
    pk = price(i)
    hi = max(hi, pk)
    best = max(best, hi - pk)

print(best)