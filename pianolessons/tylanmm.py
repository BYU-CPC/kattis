from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

g = None
matched = None
visited = None

def augmenting_path(slot):
    if visited[slot]:
        return 0
    visited[slot] = True

    for student in g[slot]:
        if matched[student] == -1 or augmenting_path(matched[student]):
            matched[student] = slot
            matched[slot] = student
            return 1
    return 0

def solve():
    global g, matched, visited

    n, m = map(int, _i().split())
    g = [[] for _ in range(n)]
    for i in range(n):
        numT, *times = map(int, _i().split())
        for t in times:
            g[i].append(n+t-1)

    matched = [-1] * (n+m)
    mcbm = 0
    for i in range(n):
        visited = [False] * n
        mcbm += augmenting_path(i)

    _p(mcbm)

solve()

stdout.flush()