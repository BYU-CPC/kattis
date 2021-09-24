from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n, p, d = map(int, _i().split())
pattern = _i()
curr = pattern[-p:].count('Z')
res = 0
for i in range(n):
    curr += (pattern[i] == 'Z') - (pattern[i-p] == 'Z')
    res += curr < d
_p(res)

stdout.flush()

# sliding window or two pointer, could do prefix sums I guess