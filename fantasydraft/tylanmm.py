from sys import stdin, stdout, setrecursionlimit
from collections import deque

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

# read input
n, k = map(int, _i().split())
qs = []
for _ in range(n):
    q, *names = _i().split()
    qs.append(deque(names))
names = deque([_i() for _ in range(int(_i()))])
namesSet = set(names)

# build up each team
final = [[] for _ in range(n)]
for _ in range(k):
    for i in range(n):
        while qs[i] and (qs[i][0] not in namesSet):
            qs[i].popleft()
        
        while names[0] not in namesSet:
            names.popleft()
        
        if qs[i]:
            name = qs[i].popleft()
        else:
            name = names.popleft()
            
        final[i].append(name)
        namesSet.remove(name)    

for lst in final:
    _p(' '.join(lst))

stdout.flush()

# queue, simulation