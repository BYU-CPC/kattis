line = input()
while line != '0 0':
    w, l = map(int, line.split())
    n = int(input())
    xFake, yFake = 0, 0
    xReal, yReal = 0, 0
    for _ in range(n):
        dir, dist = input().split()
        dist = int(dist)
        if dir == 'u':
            yFake += dist
            yReal = min(yReal + dist, l-1)
        elif dir == 'd':
            yFake -= dist
            yReal = max(yReal - dist, 0)
        elif dir == 'r':
            xFake += dist
            xReal = min(xReal + dist, w-1)
        else:
            xFake -= dist
            xReal = max(xReal - dist, 0)
    print(f'Robot thinks {xFake} {yFake}')
    print(f'Actually at {xReal} {yReal}')
    line = input()