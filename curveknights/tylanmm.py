from sys import stdin, stdout
import heapq

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

# read file, build graph
# v -> u with weight w if v requires w of u
n, m = map(int, _i().split())
amt = list(map(int, _i().split()))
adj = [[] for _ in range(n)]
in_deg = [0]*n
for _ in range(m):
    u, v, w = map(int, _i().split())
    adj[v].append((u, w))
    in_deg[u] += 1

pq = []
for i in range(n):
    if in_deg[i] == 0:
        pq.append((i, amt[i]))

while pq:
    u, qty = heapq.heappop(pq)
    for v, w in adj[u]:
        in_deg[v] -= 1
        amt[v] += qty * w
        if not in_deg[v]:
            heapq.heappush(pq, (v, amt[v]))

print(*amt)

stdout.flush()

# Kahn's, topological sort, priority queue