from collections import deque

h, t = map(int, input().split())
while h and t:
    seen = set()
    q = deque()
    q.append((h, t, 0))
    while q:
        h, t, s = q.popleft()
        if (h, t) in seen:
            continue
        
        if h == 0 and t == 0:
            print(s)
            break

        seen.add((h, t))
        
        if t == 1: 
            q.append((h, t+1, s+1))
        if t >= 2:
            q.append((h+1, t-2, s+1))
        if h >= 2:
            q.append((h-2, t, s+1))
    else:
        print(-1)
    
    h, t = map(int, input().split())