from math import pi

for _ in range(int(input())):
    r, n = map(int, input().split())
    vals = [0, r*r, r*r]
    while len(vals) <= n:
        vals.append(vals[-1] * 0.75)
    
    if n == 1:
        print(r*r*pi)
    else:
        print(sum(vals) * pi)