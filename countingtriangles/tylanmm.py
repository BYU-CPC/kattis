def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
    if val < 0:
        return 1
    elif val > 0:
        return -1
    else:
        return 0

def intersects(line1, line2):
    o1 = orientation((line1[0], line1[1]), (line1[2], line1[3]), (line2[0], line2[1]))
    o2 = orientation((line1[0], line1[1]), (line1[2], line1[3]), (line2[2], line2[3]))
    o3 = orientation((line2[0], line2[1]), (line2[2], line2[3]), (line1[0], line1[1]))
    o4 = orientation((line2[0], line2[1]), (line2[2], line2[3]), (line1[2], line1[3]))
    
    if o1 != o2 and o3 != o4:
        return True
    return False

n = int(input())
while n != 0:
    counts = 0
    lines = [tuple(map(float, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if intersects(lines[i], lines[j]):
                for k in range(j+1, n):
                    if intersects(lines[j], lines[k]) and intersects(lines[k], lines[i]):
                        counts += 1
    print(counts)
    n = int(input())