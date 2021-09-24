from itertools import combinations

def calc_score(ings):
    sour = 1
    bitter = 0
    for s, b in ings:
        sour *= s
        bitter += b
    return abs(sour - bitter)

n = int(input())
ings = [tuple(map(int, input().split())) for _ in range(n)]
lo = float('inf')
for r in range(1, n+1):
    for combo in combinations(ings, r):
        lo = min(lo, calc_score(combo))
print(lo)