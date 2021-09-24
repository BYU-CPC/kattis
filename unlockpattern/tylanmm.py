import math

locs = [0]*9
for i in range(3):
    line = list(map(int, input().split()))
    for j in range(3):
        locs[line[j]-1] = (i,j)

def calcDist(loc1, loc2):
    return math.sqrt(abs(loc2[0]-loc1[0])**2 + abs(loc2[1]-loc1[1])**2)

total = 0
for i in range(8):
    total += calcDist(locs[i], locs[i+1])

print(total)