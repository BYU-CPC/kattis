from collections import deque

isPrime = [True]*10000
for i in range(2, 10000):
    if not isPrime[i]:
        continue
    for j in range(i*i, 10000, i):
        isPrime[j] = False

for _ in range(int(input())):
    start, end = input().split()
    seen = set()
    q = deque()
    q.append((start, 0))

    while q:
        n, cost = q.popleft()
        if n in seen: continue
        seen.add(n)

        if n == end:
            print(cost)
            break

        for d in range(1, 10):
            if int(n[0]) != d and isPrime[d*1000 + int(n[1:])]:
                q.append((str(d) + n[1:], cost+1))
        
        for i in range(1, 4):
            for d in range(10):
                if int(n[i]) != d and isPrime[int(n[:i] + str(d) + n[i+1:])]:
                    q.append((n[:i] + str(d) + n[i+1:], cost+1))

    else:
        print('Impossible')