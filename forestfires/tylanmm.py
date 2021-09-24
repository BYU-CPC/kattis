from sys import stdin, stdout

def _p(x='', end='\n'):
    stdout.write(str(x) + end)

class ufds:
    def __init__(self, n):
        self.p = list(range(n+1))
        self.r = [0]*(n+1)
    
    def find(self, q):
        if self.p[q] == q:
            return q
        self.p[q] = self.find(self.p[q])
        return self.p[q]
    
    def sameset(self, p, q):
        return self.find(p) == self.find(q)
    
    def union(self, p, q):
        x, y = self.find(p), self.find(q)
        if x != y:
            if self.r[x] > self.r[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                self.r[y] += self.r[x] == self.r[y]

def rand(r):
    while True:
        r = (r*5171 + 13297) % 50021
        yield r 

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for t in stdin.readlines():
    # set up variables for this simulation
    tree = []
    sets = ufds(10000)
    r, n = map(int, t.split())
    r = rand(r)
    count = 0

    for i in range(n):
        # generate tree
        m = next(r) % 10000
        while sets.r[m]:
            m = next(r) % 10000
        sets.r[m] = 1
        tree.append(m)

        # connect to any neighboring trees
        x, y = m // 100, m % 100
        for dx, dy in dirs:
            if (0 <= x + dx < 100) and (0 <= y + dy < 100) and (sets.r[(x + dx)*100 + (y + dy)] > 0):
                sets.union(m, (x + dx)*100 + (y + dy))
        
        # find query trees
        a = tree[next(r) % (i + 1)]
        b = tree[next(r) % (i + 1)]

        # answer query
        count += sets.sameset(a, b)

        # reset success counter, if necessary
        if (i + 1) % 100 == 0:
            _p(str(count), ' ')
            count = 0

    _p()

stdout.flush()

# union find disjoint sets, ufds, simulation, pseudorandom numbers