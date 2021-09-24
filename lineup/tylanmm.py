names = [input() for _ in range(int(input()))]
inOrder = sorted(names)
if names == inOrder:
    print('INCREASING')
elif names == inOrder[::-1]:
    print('DECREASING')
else:
    print('NEITHER')