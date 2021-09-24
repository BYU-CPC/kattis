from collections import deque

for _ in range(int(input())):
    c, r = input()
    c = ord(c) - ord('a') + 1
    r = int(r)

    seen = [[False]*9 for _ in range(9)]
    q = deque()
    q.append((c, r, 0))

    while q:
        C, R, j = q.popleft()
        if seen[R][C] != False:
            continue

        seen[R][C] = j

        if C - 2 > 0:
            if R - 1 > 0:
                q.append((C-2, R-1, j+1))
            if R + 1 <= 8:
                q.append((C-2, R+1, j+1))
        
        if C + 2 <= 8:
            if R - 1 > 0:
                q.append((C+2, R-1, j+1))
            if R + 1 <= 8:
                q.append((C+2, R+1, j+1))
        
        if R - 2 > 0:
            if C - 1 > 0:
                q.append((C-1, R-2, j+1))
            if C + 1 <= 8:
                q.append((C+1, R-2, j+1))
        
        if R + 2 <= 8:
            if C - 1 > 0:
                q.append((C-1, R+2, j+1))
            if C + 1 <= 8:
                q.append((C+1, R+2, j+1))
    
    hi, hiding = 0, []
    for R in range(1, 9):
        for C in range(1, 9):
            if seen[R][C] > hi:
                hi = seen[R][C]
                hiding = [chr(C + ord('a') - 1) + str(R)]
            elif seen[R][C] == hi:
                hiding.append(chr(C + ord('a') - 1) + str(R))
    
    hiding.sort(key=lambda x: x[0])
    hiding.sort(key=lambda x: x[1], reverse=True)
    print(hi, *hiding)