a, b, c, n = map(int, input().split())
if a and b and c and n >= 3 and a+b+c >= n:
    print('YES')
else:
    print('NO')