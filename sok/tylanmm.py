a, b, c = map(int, input().split())
i, j, k = map(int, input().split())
r = min(a/i, b/j, c/k)
print(a - i*r, b - j*r, c - k*r)