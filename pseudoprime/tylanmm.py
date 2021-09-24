bound = 47000
sieve = [True]*(bound + 1)
sieve[0] = sieve[1] = False
primes = []
for i in range(2, bound+1):
    if not sieve[i]:
        continue
    primes.append(i)
    for j in range(i*i, bound+1, i):
        sieve[j] = False

def isPrime(num):
    if num <= bound:
        return sieve[num]
    for p in primes:
        if p*p > num*num: return True
        if num % p == 0:  return False
    return True

p, a = map(int, input().split())
while p and a:
    if isPrime(p):
        print('no')
        p, a = map(int, input().split())
        continue
    
    res = pow(a, p, p)
    if res == a:
        print('yes')
    else:
        print('no')

    p, a = map(int, input().split())