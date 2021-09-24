n = int(input())
houses = []
spies = []
for i in range(n):
    row = input()
    for j in range(n):
        if row[j] == 'H':
            houses.append((i, j))
        elif row[j] == 'S':
            spies.append((i, j))

def dist(h, s):
    return abs(h[0] - s[0]) + abs(h[1] - s[1])

d = 0
for s in spies:
    minDist = 200
    for h in houses:
        minDist = min(minDist, dist(h, s))
    d = max(d, minDist)

print(d)