from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n = int(_i())
sq = [int(_i()) for _ in range(n)]

# dp[square][previous jump size]
dp = [[float('inf')]*(n+1) for _ in range(n)]
dp[0][0] = 0
for jmp in range(n+1):
    for s in range(n-1, -1, -1):
        if s - jmp >= 0:
            dp[s-jmp][jmp] = min(dp[s-jmp][jmp], dp[s][jmp] + sq[s-jmp])
    for s in range(n):
        if s + jmp + 1 < n:
            dp[s+jmp+1][jmp+1] = min(dp[s+jmp+1][jmp+1], dp[s][jmp] + sq[s+jmp+1])

_p(min(dp[n-1]))

stdout.flush()