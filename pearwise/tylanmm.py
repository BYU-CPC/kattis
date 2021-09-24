from sys import stdin, stdout

def _i():
    return stdin.readline()

def _p(x):
    stdout.write(str(x) + '\n')

def dfs(u):
    seen[u] = True
    total = 1
    for v in g[u]:
        if not seen[v]:
            total += dfs(v)
    return total

n, m = map(int, _i().split())
score = [[0]*n for _ in range(n)]
for _ in range(m):
    p, ballot = _i().split()
    p = int(p)
    ballot = list(map(lambda x: ord(x) - 65, ballot))
    for i in range(n-1):
        c1 = ballot[i]
        for j in range(i+1, n):
            score[c1][ballot[j]] += p
    
g = [[] for _ in range(n)]
for i in range(n-1):
    for j in range(i+1, n):
        if score[i][j] > score[j][i]:
            g[i].append(j)
        else:
            g[j].append(i)

for i in range(n):
    seen = [False]*n
    if dfs(i) == n:
        _p(chr(i + 65) + ': can win')
    else:
        _p(chr(i + 65) + ': can\'t win')

stdout.flush()