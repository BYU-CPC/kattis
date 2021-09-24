k, t, p, q, x1 = map(int, input().split())
xs = [x1]
for _ in range(t-1):
    xs.append(((xs[-1] * p) % q))
for i in range(t):
    xs[i] %= 4

probs = []
for xi in xs:
    w = list(map(int, input().split()))
    prob1w2 = w[xi] / (w[xi] + w[xi^1])
    prob3w4 = w[xi^2] / (w[xi^2] + w[xi^3])
    prob4w3 = w[xi^3] / (w[xi^2] + w[xi^3])
    prob1w3 = w[xi] / (w[xi] + w[xi^2])
    prob1w4 = w[xi] / (w[xi] + w[xi^3])
    probs.append(prob1w2*prob3w4*prob1w3 + prob1w2*prob4w3*prob1w4)

dp = [[0]*(t+1) for _ in range(t+1)]
dp[0][0] = 1
for numTourneys in range(1, t+1):
    for numRight in range(t+1):
        dp[numTourneys][numRight] += dp[numTourneys-1][numRight] * (1 - probs[numTourneys-1])
        if numRight:
            dp[numTourneys][numRight] += dp[numTourneys-1][numRight-1] * probs[numTourneys-1]

print(sum(dp[t][k:]))