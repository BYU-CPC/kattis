from sys import stdin, stdout, setrecursionlimit

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

def solve(n, d):
    if n == 1 and d == 1:
        return 1
    if n > d:
        return 2 * solve(n-d, d) + 1
    else:
        return 2 * solve(n, d-n)

for t in range(int(_i())):
    k, frac = _i().split()
    num, den = map(int, frac.split('/'))
    _p(k + ' ' + str(solve(num, den)))

stdout.flush()

# recursion