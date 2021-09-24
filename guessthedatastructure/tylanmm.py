from sys import stdin, stdout
from collections import deque
import heapq

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

def solve():
    n = int(_i())
    s = deque()
    q = deque()
    pq = []
    isStack = True
    isQueue = True
    isPQueue = True

    for _ in range(n):
        type, x = map(int, _i().split())
        if type == 1:
            s.append(x)
            q.append(x)
            heapq.heappush(pq, -x)
        else:
            if len(s) == 0 or s.pop() != x:
                isStack = False
            if len(q) == 0 or q.popleft() != x:
                isQueue = False
            if len(pq) == 0 or heapq.heappop(pq) != -x:
                isPQueue = False

    total = isStack + isQueue + isPQueue
    if total > 1:
        _p('not sure')
    elif total == 0:
        _p('impossible')
    else:
        _p('stack' if isStack else 'queue' if isQueue else 'priority queue')

while True:
    try:
        solve()
    except Exception:
        break

stdout.flush()