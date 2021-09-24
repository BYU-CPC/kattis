x, y = map(int, input().split())
if y == 1:
    if x:
        print('IMPOSSIBLE')
    else:
        print('ALL GOOD')
else:
    if x:
        print(x/(1-y))
    else:
        print(0)