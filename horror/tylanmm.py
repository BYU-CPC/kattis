from collections import deque

n, h, l = map(int, input().split())
horror = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(l):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

index = [float('inf')]*n
for id in horror:
    index[id] = 0

def bfs(src):
    seen = [False]*n
    q = deque()
    q.append((src, 0))

    while q:
        id, ind = q.popleft()
        if seen[id]: continue
        seen[id] = True

        for to in g[id]:
            if not seen[to] and index[to] > ind+1:
                index[to] = ind+1
                q.append((to, ind+1))

for id in horror:
    bfs(id)

hi = 0
for i in range(n):
    if index[i] > index[hi]:
        hi = i
print(hi)