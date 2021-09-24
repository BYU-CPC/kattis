h, w, n = map(int, input().split())
bricks = map(int, input().split())

row = 0
rowLen = 0
for b in bricks:
    if rowLen + b < w:
        rowLen += b
    elif rowLen + b == w:
        rowLen = 0
        row += 1
    else:
        break

if row >= h:
    print('YES')
else:
    print('NO')