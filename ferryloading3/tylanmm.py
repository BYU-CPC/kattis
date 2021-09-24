from collections import deque

for _ in range(int(input())):
    n, t, m = map(int, input().split())
    side, time, queues = 0, 0, [deque(), deque()]
    for i in range(m):
        ti, si = input().split()
        queues[0 if si == 'left' else 1].append((int(ti), i))
    times = [0]*m

    while queues[0] or queues[1]:
        time = max(time, min(queues[0][0][0] if queues[0] else float('inf'), queues[1][0][0] if queues[1] else float('inf')))
        amt = 0
        while amt < n and queues[side] and queues[side][0][0] <= time:
            times[queues[side][0][1]] = str(time + t)
            queues[side].popleft()
            amt += 1
        side ^= 1
        time += t
    
    print('\n'.join(times) + '\n')