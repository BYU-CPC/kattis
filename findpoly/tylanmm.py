import sys
raw = sys.stdin.read().strip().split(';')[:-1]
groups = {}
for seg in raw:
    p1, p2 = seg.strip().split('),(')
    x1, y1 = map(int, p1[1:].split(','))
    x2, y2 = map(int, p2[:-1].split(','))
    
    if (x2, y2) in groups:
        groups[(x2, y2)].add((x1, y1))
    else:
        groups[(x2, y2)] = {(x1, y1)}
    
    if (x1, y1) in groups:
        groups[(x1, y1)].add((x2, y2))
    else:
        groups[(x1, y1)] = {(x2, y2)}

visited = set()

def dfs(point, isShape=True):
    if len(groups[point]) != 2:
        isShape = False
    for p in groups[point]:
        if p not in visited:
            visited.add(p)
            isShape &= dfs(p, isShape)
    return isShape

forms = shapes = 0
for p in groups:
    if p not in visited:
        shape = set()
        isShape = dfs(p)
        if isShape:
            shapes += 1
        forms += 1

print(forms, shapes)