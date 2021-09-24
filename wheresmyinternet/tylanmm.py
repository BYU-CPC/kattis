from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(400000)

def _i():
    return stdin.readline()

def _p(x):
    stdout.write(str(x) + '\n')

def dfs(u):
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v)
'''
class UFDS:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [1]*n
    
    def find(self, u):
        if self.p[u] == u:
            return u
        
        parent = self.find(self.p[u])
        self.p[u] = parent
        return parent
    
    def isSameSet(self, u, v):
        return self.find(u) == self.find(v)
    
    def union(self, u, v):
        x, y = self.find(u), self.find(v)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                self.rank[y] += self.rank[x] == self.rank[y]
'''
n, m = map(int, _i().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, _i().split())
    g[a].append(b)
    g[b].append(a)

visited = [False]*n
dfs(0)

conn = True
for i in range(n):
    if not visited[i]:
        _p(i+1)
        conn = False

if conn:
    _p('Connected')

stdout.flush()