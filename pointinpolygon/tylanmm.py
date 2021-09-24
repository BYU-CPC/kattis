def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
    if val < 0:
        return 1    # clockwise
    elif val > 0:
        return -1   # counterclockwise
    else:
        return 0    # colinear

def intersects(p, q, r, s):
    o1 = orientation(p, q, r)
    o2 = orientation(p, q, s)
    o3 = orientation(r, s, p)
    o4 = orientation(r, s, q)
    
    if o3 == 0 and (min(r[0], s[0]) <= p[0] <= max(r[0], s[0])) and (min(r[1], s[1]) <= p[1] <= max(r[1], s[1])):
        return -1
    if o1 != o2 and o3 != o4:
        return 1
    return 0

n = int(input())
while n:
    v = [tuple(map(int, input().split())) for _ in range(n)]
    points = [tuple(map(int, input().split())) for _ in range(int(input()))]
    v.append(v[0])

    for p in points:
        cross = 0
        end = [p[0] + 20983, p[1] + 20981]
        for i in range(n):
            inter = intersects(p, end, v[i], v[i+1])
            if inter == -1:
                print('on')
                break
            cross += inter
        else:
            print('in' if cross % 2 else 'out')

    n = int(input())