class BIT:
    def __init__(self, n):
        self.arr = [0]*(n+1)
        self.cap = n
    
    def range_update(self, i, j):
        self.update(i, 1)
        self.update(j+1, -1)

    def update(self, key, val):
        while key <= self.cap:
            self.arr[key] += val
            key += key & -key
    
    def query(self, key):
        res = 0
        while key:
            res += self.arr[key]
            key ^= key & -key
        return res

from sys import stdin
from math import ceil

n, k = map(int, stdin.readline().split())
rupq = BIT(101000)
s, e = 100001, 0
for _ in range(n):
    t = int(stdin.readline()) + 1
    s = min(s, t)
    e = max(e, t)
    rupq.range_update(t, t+999)

hi = 0
for i in range(s, e+1):
    hi = max(hi, rupq.query(i))
print(ceil(hi/k))