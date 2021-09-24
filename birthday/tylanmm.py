from sys import stdin, stdout

def _i():
    return stdin.readline()

def _p(x):
    stdout.write(str(x) + '\n')

num = []
low = []
parent = []
visited = [0]
bridges = set()

def findBridges(u):
    low[u] = num[u] = visited[0]
    visited[0] += 1
    for v in g[u]:
        if num[v] == -1:
            parent[v] = u
            findBridges(v)
            if num[u] < low[v]:
                bridges.add((u, v))
            low[u] = min(low[u], low[v])
        elif v != parent[u]:
            low[u] = min(low[u], num[v])

def dfs(u):
    seen[u] = True
    for v in g[u]:
        if not seen[v]:
            dfs(v)

p, c = map(int, _i().split())
while p and c:
    g = [[] for _ in range(p)]
    for _ in range(c):
        a, b = map(int, _i().split())
        g[a].append(b)
        g[b].append(a)
    
    seen = [False]*p
    dfs(0)
    if sum(seen) != p:
        _p('Yes')
    else:
        num = [-1]*p
        low = [-1]*p
        parent = [-1]*p
        visited[0] = 0
        bridges = set()
        findBridges(0)
        _p('Yes' if bridges else 'No')

    p, c = map(int, _i().split())

stdout.flush()