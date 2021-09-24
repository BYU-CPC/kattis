from sys import stdin

primes = []
isPrime = [True]*47000
isPrime[0] = isPrime[1] = False
for i in range(2, 47000):
    if not isPrime[i]:
        continue
    primes.append(i)
    for j in range(i*i, 47000, i):
        isPrime[j] = False

def printFactorization(n):
    factors = {}
    if n < 0:
        factors[-1] = 1
        n = -n
    
    prime, pI = 2, 0
    while prime*prime <= n:
        if n % prime == 0:
            if prime not in factors:
                factors[prime] = 0
            factors[prime] += 1
            n //= prime
        else:
            pI += 1
            prime = primes[pI]
    
    if n != 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1

    res = []
    for f in factors:
        if factors[f] == 1:
            res.append(str(f))
        else:
            res.append(f'{f}^{factors[f]}')
    
    print(' '.join(res))

for line in stdin.readlines():
    printFactorization(int(line))