for i in range(int(input())):
    r, e, c = tuple(map(int, input().split()))
    if r > e - c:
        print('do not advertise')
    elif r == e - c:
        print('does not matter')
    else:
        print('advertise')