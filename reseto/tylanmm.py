n, k = map(int, input().split())
sieve = [True]*(n+1)
sieve[0] = sieve[1] = False

def solve():
    count = 0
    for i in range(2, n+1):
        if not sieve[i]:
            continue
        count += 1
        if count == k:
            print(i)
            return
        for j in range(i*i, n+1, i):
            if sieve[j]:
                count += 1
                if count == k:
                    print(j)
                    return
            sieve[j] = False

solve()