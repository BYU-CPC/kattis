from math import asin, acos, atan, pi

n = int(input())
trees = [tuple(map(int, input().split())) for _ in range(n)]
b, d = map(int, input().split())

rem = []
for x, y, r in trees:
    dist = (x*x + y*y)**0.5
    # if it's too far away to cause an issue
    if d + b <= dist - r:
        continue
    
    a = acos(x/dist)
    if y < 0:
        a = 2*pi - a
    # if it's close enough that the entire slice will be taken out
    if d >= dist:
        z = asin((b+r)/dist)
    else:
        z = acos((d*d + dist*dist - (b + r)**2) / (2 * d * dist))
    rem.append([a-z, a+z])

# condense ranges
rem.sort()
i = 0
while i < len(rem):
    j = (i + 1) % len(rem)
    if i == j:
        break
    elif rem[i][0] <= rem[j][0] <= rem[i][1]:
        rem[i][1] = max(rem[i][1], rem[j][1])
        rem.pop(j)
    elif rem[i][0] <= rem[j][0] + 2*pi <= rem[i][1]:
        rem[i][1] = max(rem[i][1], rem[j][1]+2*pi)
        rem.pop(j)
    else:
        i += 1

total = 2*pi
for s, e in rem:
    total -= e - s
print(max(0, total / (2*pi)))