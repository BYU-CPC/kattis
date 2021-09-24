line = input()
while line != '0 0 0.0':
    x, y, w = line.split()
    x, y, w = int(x), int(y), float(w)
    xs = sorted(list(map(float, input().split())))
    ys = sorted(list(map(float, input().split())))

    canDoIt = True
    if not x or xs[0] > w/2:
        print('NO')
        line = input()
        continue
    for i in range(1, x):
        if xs[i-1] + w < xs[i]:
            canDoIt = False
            break
    
    if not canDoIt or 75 > (xs[-1] + w/2) or not y or ys[0] > w/2:
        print('NO')
        line = input()
        continue
    for i in range(1, y):
        if ys[i-1] + w < ys[i]:
            canDoIt = False
            break
    
    if not canDoIt or 100 > (ys[-1] + w/2):
        print('NO')
        line = input()
        continue

    if canDoIt:
        print('YES')
    line = input()