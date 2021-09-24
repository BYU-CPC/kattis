from sys import stdin

# Run sieve up through largest possible n
primes = []
isPrime = [True] * 432
isPrime[0] = isPrime[1] = False
for i in range(2, 432):
    if not isPrime[i]:
        continue
    primes.append(i)
    for j in range(i*i, 432, i):
        isPrime[j] = False

def getPrimeFactors(n):
    factors = {}
    pI, prime = 0, 2
    while prime**2 <= n:
        if n % prime == 0:
            if prime not in factors:
                factors[prime] = 0
            factors[prime] += 1
            n //= prime
        else:
            pI += 1
            prime = primes[pI]
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors

# Pre-calculate prime factors for every number up through n
factors = [getPrimeFactors(i) for i in range(432)]

for line in stdin.readlines():
    n, k = map(int, line.split())
    k = min(k, n-k)     # n C k == n C (n-k)
    facts = {}
    for i in range(1, k+1):
        for f in factors[n-i+1]:
            if f not in facts:
                facts[f] = 0
            facts[f] += factors[n-i+1][f]
        
        for f in factors[i]:
            if f not in facts:
                facts[f] = 0
            facts[f] -= factors[i][f]
    
    divisors = 1
    for f in facts:
        divisors *= facts[f] + 1
    print(divisors)