class BIT:
    def __init__(self, n):
        self.arr = [0]*(n+1)
        self.bits = [0]*(n+1)
        self.cap = n
    
    def update(self, key):
        self.bits[key] ^= 1
        val = 1 * (1 if self.bits[key] else -1)
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

n, k = map(int, stdin.readline().split())
fen = BIT(n)
for _ in range(k):
    line = stdin.readline().split()
    if line[0] == 'F':
        fen.update(int(line[1]))
    else:
        l, r = int(line[1]), int(line[2])
        stdout.write(str(fen.query(r) - fen.query(l-1)) + '\n')

stdout.flush()