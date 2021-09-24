from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(20000)

def _i():
    return stdin.readline()

def _p(x):
    stdout.write(str(x) + '\n')

def dfs(d):
    visited[d] = True
    for dom in g[d]:
        if not visited[dom]:
            dfs(dom)

for t in range(int(_i())):
    n, m, l = map(int, _i().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(lambda x: int(x)-1, _i().split())
        g[x].append(y)
    
    visited = [False]*n
    for _ in range(l):
        dfs(int(_i())-1)
    
    _p(sum(visited))

stdout.flush()