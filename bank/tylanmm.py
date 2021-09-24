import heapq

n, t = map(int, input().split())
cust = [tuple(map(int, input().split())) for _ in range(n)]
q = [0]*t
for ci, ti in cust:
    for i in range(ti, -1, -1):
        if ci > q[i]:
            ci, q[i] = q[i], ci
print(sum(q))