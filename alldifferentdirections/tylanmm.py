from math import sin, cos, pi

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

n = int(input())
while n:
    dest = []
    for _ in range(n):
        line = input().split()
        theta = 0
        x, y = float(line[0]), float(line[1])
        for i in range(2, len(line), 2):
            comm, val = line[i], float(line[i+1])
            if comm == 'start':
                theta = val
            elif comm == 'turn':
                theta += val
            else:
                x += val * cos(theta * pi / 180)
                y += val * sin(theta * pi / 180)
        dest.append((x, y))
    
    mean = [0, 0]
    for x, y in dest:
        mean[0] += x
        mean[1] += y
    mean[0] /= n
    mean[1] /= n

    worst = dist(max(dest, key=lambda p: dist(p, mean)), mean)
    print(mean[0], mean[1], worst)

    n = int(input())