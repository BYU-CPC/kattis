primes = []
sieve = [False]*1001
sieve[0] = sieve[1] = True
for i in range(2, 1001):
    if sieve[i]:
        continue
    primes.append(i)
    for j in range(i*i, 1001, i):
        sieve[j] = True

def findPQ(n):
    for p in primes:
        if n % p == 0:
            return p, n // p

def findD(n, e):
    p, q = findPQ(n)
    phi = (p-1)*(q-1)
    for d in range(2, phi):
        if d*e % phi == 1:
            return d

for _ in range(int(input())):
    n, e = map(int, input().split())
    print(findD(n, e))