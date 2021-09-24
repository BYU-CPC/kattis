def calcXs(h, k):
    det = k * (h*h + k*k - 1)**0.5
    return (h + det)/(h*h + k*k), (h - det)/(h*h + k*k)

def solve(p):
    if p[0]:
        if p[1]:
            x1, x2 = calcXs(p[0], p[1])
        else:
            x1 = x2 = 1 / p[0]
        y1 = (1 - min(x1*x1, 1))**0.5
        y2 = (1 - min(x2*x2, 1))**0.5
    else:
        y1 = y2 = 1 / p[1]
        x1 = -(1 - min(y1*y1, 1))**0.5
        x2 = -x1

    if p[0] < -1:
        y2 *= -1
    elif p[0] > 1:
        y1 *= -1
    elif p[1] < 0:
        y1 *= -1
        y2 *= -1
    
    if abs(x1 - p[0]) < 0.000001:
        a1, b1, c1 = 1, 0, x1
    else:
        a1, b1, c1 = -(p[1] - y1), (p[0] - x1), (p[0] - x1)*p[1] - (p[1] - y1)*p[0]
    
    if abs(x2 - p[0]) < 0.000001:
        a2, b2, c2 = 1, 0, x2
    else:
        a2, b2, c2 = -(p[1] - y2), (p[0] - x2), (p[0] - x2)*p[1] - (p[1] - y2)*p[0]
    
    print(f'({a1:.6f},{b1:.6f},{c1:.6f},{a2:.6f},{b2:.6f},{c2:.6f})')

points = [tuple(map(float, input().split())) for _ in range(int(input()))]
for p in points:
    solve(p)