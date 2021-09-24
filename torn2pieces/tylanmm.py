n = int(input())
g = {}

for _ in range(n):
    src, *stations = input().split()
    if src not in g:
        g[src] = []
    
    for s in stations:
        g[src].append(s)
        if s not in g:
            g[s] = [src]
        else:
            g[s].append(src)

start, end = input().split()

seen = set()
path = []
def dfs(src):
    seen.add(src)
    if src == end:
        path.append(end)
        return True
    
    for s in g[src]:
        if s not in seen:
            if dfs(s):
                path.append(src)
                return True
    return False

if start not in g or end not in g:
    print('no route found')
elif dfs(start):
    print(' '.join(path[::-1]))
else:
    print('no route found')