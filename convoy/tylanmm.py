from collections import deque
from heapq import *

n, k = map(int, input().split())
speeds = [int(input()) for _ in range(n)]
speeds.sort()

left = deque([(speeds[i], i) for i in range(n)])
stad = []
time = 0
while left:
    if stad and (left[0][0] > stad[0][0] or k == 0):
        t, i = heappop(stad)
        k += 1
    else:
        t, i = left.popleft()

    for _ in range(min(len(left), 4)):
        left.pop()
    time = max(time, t)
    heappush(stad, (t + speeds[i]*2, i))
    k -= 1
print(time)

# 10 at house, 1st goes 4500, 2nd goes 10000, rest 1000000