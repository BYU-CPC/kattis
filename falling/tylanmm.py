d = int(input())
for n in range(100002):
    n2 = (n*n + d)**0.5
    if abs(n2 - int(n2)) < 0.000001:
        print(n, int(n2))
        break
else:
    print('impossible')