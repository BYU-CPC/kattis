for _ in range(int(input())):
    line = list(map(int, input().split()))
    m, line = line[0], line[1:]
    points = [(line[2*i], line[2*i+1]) for i in range(m)]
    points.append(points[0])
    
    total = 0
    for i in range(m):
        total += points[i][0]*points[i+1][1] - points[i][1]*points[i+1][0]
    print(total / 2)