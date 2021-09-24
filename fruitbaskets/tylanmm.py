n = int(input())
weights = list(map(int, input().split()))

def solve(i, total):
    if i == n or total >= 200:
        return 0
    
    totalWeight = 0
    if total + weights[i] < 200:
        totalWeight += total + weights[i]
    totalWeight += solve(i+1, total)
    totalWeight += solve(i+1, total + weights[i])
    return totalWeight

print((2**(n - 1)) * sum(weights) - solve(0, 0))