n, m, s, t = map(int, input().split())
g = [set() for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x].add(y)
    g[y].add(x)

prev = {s: 1}
for _ in range(t):
    curr = {}
    for u in prev:
        for v in g[u]:
            if v not in curr:
                curr[v] = 0
            curr[v] += prev[u]
    prev = curr
print(sum(prev.values()))