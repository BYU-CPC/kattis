from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n, p = map(int, _i().split())
dist = sorted(map(int, _i().split()))
_p(max([p*(i+1) - (d - dist[0]) for i, d in enumerate(dist)]))

stdout.flush()