from sys import stdin, stdout, setrecursionlimit

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

def solve(n):
    if n == 1:
        return 1, 1
    num, den = solve(n//2)
    if n % 2:
        return num+den, den
    else:
        return num, den+num

for t in range(int(_i())):
    k, n = map(int, _i().split())
    num, den = solve(n)
    _p('%d %d/%d' % (k, num, den))

stdout.flush()