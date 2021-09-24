n, *v = list(map(int, input().split()))

def solve(v):
    if all([val == v[0] for val in v]):
        return 0, v[-1]
    
    newV = []
    for i in range(1, len(v)):
        newV.append(v[i] - v[i-1])
    deg, diff = solve(newV)
    return deg+1, v[-1] + diff

deg, diff = solve(v)
print(deg, diff)

# recursion, list, array