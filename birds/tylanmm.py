l, d, n = map(int, input().split())
birds = [int(input()) for _ in range(n)]
birds.sort()

total = 0
if n:
    for i in range(n-1):
        dist = (birds[i+1] - birds[i]) // d
        total += dist - 1
    total += (birds[0] - 6) // d
    total += (l - 6 - birds[-1]) // d
elif l >= 12:
    total = (l - 12) // d + 1
print(total)