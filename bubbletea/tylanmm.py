n, pTea = int(input()), list(map(int, input().split()))
m, pTop = int(input()), list(map(int, input().split()))
lo = float('inf')
for i in range(n):
    for top in list(map(int, input().split()))[1:]:
        lo = min(pTea[i] + pTop[top-1], lo)
x = int(input())
print(0 if lo > x else x//lo - 1)