isPrime = [True]*20001
isPrime[0] = isPrime[1] = False
for i in range(2, 20001):
    if not isPrime[i]:
        continue
    for j in range(i*i, 20001, i):
        isPrime[j] = False

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

for _ in range(int(input())):
    n, d = map(int, input().split())
    flowers = [(0,0)] + [tuple(map(int, input().split())) for _ in range(n)]
    travel, i = 0, 1
    maxFlowers = 0
    while i <= n and dist(flowers[i-1], flowers[i]) + travel <= d:
        travel += dist(flowers[i-1], flowers[i])
        if isPrime[i]:
            maxFlowers = i
        i += 1
    print(maxFlowers)