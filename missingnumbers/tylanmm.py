n, i = int(input()), 1
for _ in range(n):
    num = int(input())
    while i < num:
        print(i)
        i += 1
    i += 1
if i-1 == n:
    print('good job')