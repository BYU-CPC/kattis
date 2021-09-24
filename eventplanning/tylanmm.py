n, b, h, w = map(int, input().split())
lo = float('inf')
for _ in range(h):
    p = int(input())
    for a in map(int, input().split()):
        if a >= n and p * n <= b:
            lo = min(lo, p * n)
print('stay home' if lo == float('inf') else lo)