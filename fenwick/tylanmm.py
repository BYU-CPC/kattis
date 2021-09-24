from sys import stdin, stdout

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

n, q = map(int, stdin.readline().split())
fen = BIT(n)

for _ in range(q):
    line = stdin.readline().split()
    if line[0] == '+':
        k, v = int(line[1]), int(line[2])
        fen.update(k+1, v)
    else:
        k = int(line[1])
        stdout.write(str(fen.query(k)) + '\n')

stdout.flush()