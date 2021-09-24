def solve(r, s, x, y, w):
    dp = [[0]*(y+1) for _ in range(y+1)]
    dp[0][0] = 1
    for numDiceUsed in range(1, y+1):
        for numHigher in range(y+1):
            dp[numDiceUsed][numHigher] += dp[numDiceUsed-1][numHigher]*(r-1)
            if numHigher:
                dp[numDiceUsed][numHigher] += dp[numDiceUsed-1][numHigher-1]*(s-r+1)
    
    count = sum(dp[y][x:])
    return 'yes' if (count / s**y) * w > 1 else 'no'

for _ in range(int(input())):
    r, s, x, y, w = map(int, input().split())
    print(solve(r, s, x, y, w))