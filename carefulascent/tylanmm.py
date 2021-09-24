x, y = map(int, input().split())
n = int(input())
shields = [tuple(map(float, input().split())) for _ in range(n)]
den, total = 0, 0
for l, u, f in shields:
    den += f * (u - l)
    total += u - l
s = x / (y - total + den)
print(s)

# sum shield amounts
# y - total = normal amount
# say that his speed is s
# then s(y-total) + s(f1)(u1 - l1) + s(f2)(u2 - l2) + ... + s(fn)(un - ln) =  x
# do the algebra