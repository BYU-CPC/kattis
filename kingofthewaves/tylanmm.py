n = int(input())
mat = [list(input()) for _ in range(n)]

visited = [False]*n
top = []
def dfs(i):
    visited[i] = True
    for j in range(n):
        if not visited[j] and mat[i][j] == '1':
            dfs(j)
    top.append(i)

dfs(0)
if len(top) == n:
    print(' '.join(map(str, top)))
else:
    print('impossible')