primes = []
isPrime = [True]*47000
isPrime[0] = isPrime[1] = False
for i in range(2, 47000):
    if not isPrime[i]:
        continue
    primes.append(i)
    for j in range(i*i, 47000, i):
        isPrime[j] = False

def gcd(a, b):
    return gcd(b, a % b) if b else a

def gcdOfExps(factors):
    gcf = 0
    for f in factors:
        gcf = gcd(factors[f], gcf)
    return gcf

def getFactors(n):
    factors = {}
    if n < 0:
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
    return factors

def getPthPower(n):
    factors = getFactors(n)
    gcf = gcdOfExps(factors)
    if n > 0 or gcf % 2 == 1:
        return gcf
    while gcf % 2 == 0:
        gcf //= 2
    return gcf

x = int(input())
while x:
    print(getPthPower(x))
    x = int(input())