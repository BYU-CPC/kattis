c, x, m = map(float, input().split())
c, hi = c/2, 0
for _ in range(6):
    s, mpg = input().split()
    s, mpg = int(s), float(mpg)
    t = m / s
    if (c - (t * x)) * mpg >= m:
        hi = s
print(f'YES {hi}' if hi else 'NO')