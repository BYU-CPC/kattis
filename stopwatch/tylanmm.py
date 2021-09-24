n = int(input())
isRunning = False
ans = 0
last = 0
for _ in range(n):
    t = int(input())
    ans += (t - last) if isRunning else 0
    last = t
    isRunning ^= 1
print('still running' if isRunning else ans)