def solve(n, parties):
    dp = [[0]*151 for _ in range(n+1)]
    for i in range(n): dp[i][0] = 1
    
    for numConsidered in range(1, n+1):
        for numSeats in range(1, 151):
            if dp[numConsidered-1][numSeats-parties[numConsidered-1][0]]:
                dp[numConsidered][numSeats] = dp[numConsidered-1][numSeats-parties[numConsidered-1][0]] * (parties[numConsidered-1][1] / 100)
            dp[numConsidered][numSeats] = max(dp[numConsidered][numSeats], dp[numConsidered-1][numSeats])
    
    return max(dp[n][76:])*100

for _ in range(int(input())):
    n = int(input())
    parties = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, parties))