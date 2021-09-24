def gcd(a, b):
    return gcd(b, a % b) if b else a

n = int(input())
rings = list(map(int, input().split()))
for i in range(1, n):
    a, b = rings[0], rings[i]
    if a < b:
        a, b = b, a
    gcf = gcd(a, b)
    print(f'{rings[0]//gcf}/{rings[i]//gcf}')