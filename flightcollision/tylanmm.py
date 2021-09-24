import heapq
from decimal import Decimal
# just need to use a class to improve accuracy
n = int(input())
left = list(range(-1, n+1))
right = list(range(1, n+2))
right[n] = 0

x = [0]*(n+1)
v = [0]*(n+1)
for i in range(n):
    xi, vi = map(int, input().split())
    x[i+1] = xi
    v[i+1] = vi

def calcTime(i, j):
    if v[j] == v[i]: return float('inf')
    t = Decimal(x[i] - x[j]) / Decimal(v[j] - v[i])
    return t if t > 0 else float('inf')

q = [(calcTime(i-1, i), i-1, i) for i in range(2, n+1)]
heapq.heapify(q)

hit = [False]*(n+1)
hit[0] = True

while q:
    t, i, j = heapq.heappop(q)
    
    # neither has been hit yet, and they have a finite collision time
    if not (hit[i] or hit[j]) and t != float('inf'):
        hit[i] = hit[j] = True
        right[left[i]] = right[j]
        left[right[j]] = left[i]
        heapq.heappush(q, (calcTime(left[i], right[j]), left[i], right[j]))

print(hit.count(False))
for i in range(1, n+1):
    if not hit[i]:
        print(i, end=' ')