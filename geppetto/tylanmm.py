n, m = map(int, input().split())
nope = set()
for _ in range(m):
    a, b = map(int, input().split())
    if b < a: a, b = b, a
    a -= 1
    b -= 1
    nope.add((a, b))

i, hi, count = 0, 2**n, 0
while i < hi:
    for a, b in nope:
        if i == (i | (1 << a) | (1 << b)):
            i += 1 << a
            break
    else:
        count += 1
        i += 1
print(count)