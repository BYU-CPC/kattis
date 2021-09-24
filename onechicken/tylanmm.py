n, m = map(int, input().split())
if n < m:
    print('Dr. Chaz will have %d %s of chicken left over!' % (m-n, 'piece' if m-n == 1 else 'pieces'))
else:
    print('Dr. Chaz needs %d more %s of chicken!' % (n-m, 'piece' if n-m == 1 else 'pieces'))