tests = [int(input()) for _ in range(int(input()))]
bound = max(tests)

sieve = [False]*(bound+1)
sieve[0] = sieve[1] = True
primes = []
for i in range(2, bound+1):
    if sieve[i]:
        continue
    primes.append(i)
    for j in range(i*i, bound+1, i):
        sieve[j] = True

for x in tests:
    reps = []
    for p in primes:
        if p > x/2:
            break
        if not sieve[x-p]:
            reps.append((p, x-p))
    print(f'{x} has {len(reps)} representation(s)')
    for a, b in reps:
        print(f'{a}+{b}')
    print()