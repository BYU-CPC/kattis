n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

arr = []
for i in range(n):
    total = 0
    for j in range(n):
        total |= mat[i][j]
    arr.append(str(total))
print(' '.join(arr))