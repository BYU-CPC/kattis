l, w, n, r = map(int, input().split())
cranes = [tuple(map(int, input().split())) for _ in range(n)]
walls = [(-l/2, 0), (l/2, 0), (0, -w/2), (0, w/2)]

def dist(A, B):
    return ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5

for i in range(n):
    reach = 0
    for w in walls:
        reach <<= 1
        if dist(cranes[i], w) <= r:
            reach += 1
    cranes[i] = reach

def solve():
    lo = 5
    for i in range(n):
        if cranes[i] == 15:
            lo = 1
        for j in range(i+1, n):
            if cranes[i] | cranes[j] == 15:
                lo = min(lo, 2)
            for k in range(j+1, n):
                if cranes[i] | cranes[j] | cranes[k] == 15:
                    lo = min(lo, 3)
                for l in range(k+1, n):
                    if cranes[i] | cranes[j] | cranes[k] | cranes[l] == 15:
                        lo = min(lo, 4)
    return lo if lo < 5 else 'Impossible'

print(solve())