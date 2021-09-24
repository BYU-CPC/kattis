from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

g = None
matched = None
visited = None

def augmenting_path(goph):
    if visited[goph]:
        return 0
    visited[goph] = True

    for h in g[goph]:
        if matched[h] == -1 or augmenting_path(matched[h]):
            matched[h] = goph
            matched[goph] = h
            return 1
    return 0

def solve():
    global g, matched, visited

    n, m, s, v = map(int, _i().split())
    gopher = [tuple(map(float, _i().split())) for _ in range(n)]
    hole = [tuple(map(float, _i().split())) for _ in range(m)]
    
    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            x1, y1 = gopher[i]
            x2, y2 = hole[j]
            if (x1 - x2)**2 + (y1 - y2)**2 <= (s*v)**2:
                g[i].append(j+n)

    matched = [-1] * (n+m)
    mcbm = 0
    for i in range(n):
        visited = [False] * n
        mcbm += augmenting_path(i)

    _p(max(0, n - mcbm))

while True:
    try:
        solve()
    except ValueError:
        break

stdout.flush()