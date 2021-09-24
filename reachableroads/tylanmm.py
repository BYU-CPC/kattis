def dfs(node):
    visited[node] = True
    for neighbor in g[node]:
        if not visited[neighbor]:
            dfs(neighbor)

for _ in range(int(input())):
    m = int(input())
    g = [[] for _ in range(m)]
    for i in range(int(input())):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    
    visited = [False]*m
    comp_num = 0
    for i in range(m):
        if not visited[i]:
            comp_num += 1
            dfs(i)
    print(comp_num - 1)