c, n, m = tuple(map(int, input().split()))
farms = [int(input()) for _ in range(n)]
days = [int(input()) for _ in range(m)]

daysUntilDouble = []

for f in farms:
    d = 0
    while f <= c//2:
        f *= 2
        d += 1
    daysUntilDouble.append(d)

for d in days:
    total = 0
    for i in range(n):
        if daysUntilDouble[i] >= d:
            total += 1
        else:
            total += 2 ** (d - daysUntilDouble[i])
    print(total)