for _ in range(int(input())):
    m, dists = int(input()), list(map(int, input().split()))
    prev = {0: [2, '']}
    for d in dists:
        curr = {}
        for h in prev:
            hi, dirs = prev[h]
            if h + d in curr:
                curr[h+d] = min(curr[h+d], [max(hi, h+d+2), dirs + 'U'])
            else:
                curr[h+d] = [max(hi, h+d+2), dirs + 'U']
            
            if h - d >= 0:
                if h - d in curr:
                    curr[h-d] = min(curr[h-d], [hi, dirs + 'D'])
                else:
                    curr[h-d] = [hi, dirs + 'D']
        prev = curr
    
    best = None
    for h in prev:
        hi, dirs = prev[h]
        if h == 0:
            if best == None:
                best = (h, dirs, hi)
            elif hi < best[2]:
                best = (h, dirs, hi)
    if best == None:
        print('IMPOSSIBLE')
    else:
        print(best[1])