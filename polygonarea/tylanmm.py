n = int(input())
while n:
    points = [tuple(map(int, input().split())) for _ in range(n)]
    points.append(points[0])
    total = 0
    for i in range(n):
        total += points[i][0]*points[i+1][1] - points[i][1]*points[i+1][0]
    total /= 2
    
    if total < 0:
        print('CW', -total)
    else:
        print('CCW', total)

    n = int(input())