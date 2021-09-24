bound = 50000
sieve = [False]*(bound+1)
sieve[0] = sieve[1] = True
primes = []
for i in range(2, bound+1):
    if sieve[i]:
        continue
    primes.append(i)
    for j in range(i*i, bound+1, i):
        sieve[j] = True

def isPrime(num):
    if num <= bound:
        return not sieve[num]
    for p in primes:
        if p*p > num:
            return True
        if num % p == 0:
            return False
    return True

n = int(input())
while n:
    prime = isPrime(n)
    i = 2*n + 1
    while not isPrime(i):
        i += 2
    print(str(i) + ('' if prime else f' ({n} is not prime)'))
    n = int(input())