class BIT:
    def __init__(self, n):
        self.arr = [0]*(n+1)
        self.cap = n
    
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

from sys import stdin, stdout

n, q = map(int, stdin.readline().split())
gemVals = [0] + list(map(int, stdin.readline().split()))
bits = [0] + [BIT(n) for _ in range(6)]
gems = list(stdin.readline().strip())
for i in range(n):
    g = int(gems[i])
    bits[g].update(i+1, 1)

for _ in range(q):
    op, a, b = map(int, stdin.readline().split())
    if op == 1:
        g = int(gems[a-1])
        gems[a-1] = b
        bits[g].update(a, -1)
        bits[b].update(a, 1)
    elif op == 2:
        gemVals[a] = b
    else:
        total = 0
        for i in range(1, 7):
            total += gemVals[i] * (bits[i].query(b) - bits[i].query(a-1))
        stdout.write(str(total) + '\n')

stdout.flush()