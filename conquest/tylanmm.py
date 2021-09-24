from sys import stdin, stdout, setrecursionlimit
import heapq

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

n, m = map(int, _i().split())
g = [set() for _ in range(n)]
size = [0] * n
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, _i().split())
    g[u].add(v)
    g[v].add(u)

for i in range(n):
    size[i] = int(input())

army = 0
q = [(size[0], 0)]
seen = [False]*n
seen[0] = True
while q:
    s, u = heapq.heappop(q)
    if u != 0 and s >= army:
        continue
    army += s
    for v in g[u]:
        if not seen[v]:
            seen[v] = True
            heapq.heappush(q, (size[v], v))

print(army)

stdout.flush()