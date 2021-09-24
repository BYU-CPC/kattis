ways = []
def solve(n, colors, hid):
    global ways
    ways = []
    used = [False]*n
    for i in range(n):
        paint(i, used, colors, hid, [colors[i]])

def paint(i, used, colors, hid, way):
    used[i] = True
    if all(used):
        ways.append(way.copy())
    
    for j in range(len(colors)):
        if not used[j] and (colors[j] not in hid[colors[i]]):
            way.append(colors[j])
            paint(j, used, colors, hid, way)
            way.pop()
    used[i] = False

for _ in range(int(input())):
    n = int(input())
    colors = input().split()
    hid = {c:set() for c in colors}
    for _ in range(int(input())):
        c1, c2 = input().split()
        hid[c1].add(c2)
        hid[c2].add(c1)
    
    solve(n, colors, hid)
    print(len(ways))
    print(' '.join(ways[0]))

# recursion