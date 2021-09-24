from functools import cmp_to_key

F, B = map(int, input().split())
front = list(map(int, input().split()))
back = list(map(int, input().split()))

pairs = []
for f in front:
    for b in back:
        pairs.append((f, b))

def cmp(a, b):
    if a[0]*b[1] == a[1]*b[0]:
        return -1 if a[0] < b[0] else 1
    return -1 if a[0]*b[1] < a[1]*b[0] else 1

pairs.sort(key=cmp_to_key(cmp))
for f, b in pairs:
    print(f'({f},{b})')