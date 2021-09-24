from sys import stdin, stdout
from collections import deque

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

class Teque:

    def __init__(self):
        self.f = deque()
        self.b = deque()
    
    def pushback(self, x):
        self.b.append(x)
    
    def pushfront(self, x):
        self.f.appendleft(x)
    
    def pushmiddle(self, x):
        self.balance()
        self.b.appendleft(x)
    
    def get(self, i):
        if i < len(self.f):
            return self.f[i]
        return self.b[i - len(self.f)]

    def balance(self):
        while len(self.b) < len(self.f):
            self.b.appendleft(self.f.pop())
        while len(self.f) < len(self.b):
            self.f.append(self.b.popleft())

t = Teque()
for _ in range(int(_i())):
    op, x = _i().split()
    x = int(x)
    if op == 'push_back':
        t.pushback(x)
    elif op == 'push_front':
        t.pushfront(x)
    elif op == 'push_middle':
        t.pushmiddle(x)
    else: # op == 'get'
        _p(t.get(x))

stdout.flush()