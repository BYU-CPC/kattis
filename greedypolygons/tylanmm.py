import math

for _ in range(int(input())):
    n, l, d, g = map(int, input().split())
    total = n * l * d * g
    total += math.pi * (g*d)**2
    total += .125 * (l**2) * math.tan(math.radians(90*(n-2)/n)) * 2 * n
    print(total)