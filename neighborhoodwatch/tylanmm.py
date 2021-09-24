n, k = map(int, input().split())
safe = [0] + [int(input()) for _ in range(k)] + [n+1]
total = n * (n + 1) // 2
for i in range(1, k+2):
    dist = safe[i] - safe[i-1] - 1
    total -= dist * (dist + 1) // 2
print(total)