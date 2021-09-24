from sys import stdin, stdout, setrecursionlimit
from collections import deque

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x='', end='\n'):
    stdout.write(str(x))
    stdout.write(end)

n = int(_i())
vals = list(map(int, _i().split()))
left = list(range(-1, n))
right = list(range(1, n+1))
right[-1] = -1

q = deque(range(n))
leave = []
gone = [False]*n
while q:
    curr = deque()
    leaving = []
    while q:
        i = q.popleft()
        if gone[i]: continue
        if (left[i] > -1 and vals[i] < vals[left[i]]) or (right[i] > -1 and vals[i] < vals[right[i]]):
            leaving.append(i)
            gone[i] = True
            
    for i in leaving:
        if left[i] > -1:
            right[left[i]] = right[i]
            curr.append(left[i])
        if right[i] > -1:
            left[right[i]] = left[i]
            curr.append(right[i])
    
    if leaving:
        leave.append(leaving)
    
    q = curr

_p(len(leave))
for t in leave:
    for i in t:
        _p(vals[i], ' ')
    _p()
    
for i in range(n):
    if not gone[i]:
        _p(vals[i], ' ')
_p()