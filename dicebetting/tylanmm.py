n, s, k = map(int, input().split())

dp = [[0]*(s+1) for _ in range(n+1)]
dp[0][0] = 1
for numThrows in range(1, n+1):
    for numUnique in range(1, s+1):
        dp[numThrows][numUnique] = dp[numThrows-1][numUnique-1] * (s - numUnique + 1) / s
        dp[numThrows][numUnique] += dp[numThrows-1][numUnique] * numUnique / s

print(sum(dp[n][k:]))