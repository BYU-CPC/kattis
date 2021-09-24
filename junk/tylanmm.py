from math import sqrt
for _ in range(int(input())):
    x1, y1, z1, r1, vx1, vy1, vz1 = map(int, input().split())
    x2, y2, z2, r2, vx2, vy2, vz2 = map(int, input().split())
    dx, dy, dz = x1 - x2, y1 - y2, z1 - z2
    dvx, dvy, dvz = vx1 - vx2, vy1 - vy2, vz1 - vz2

    A = dvx**2 + dvy**2 + dvz**2
    B = (dx * dvx + dy * dvy + dz * dvz) * 2
    C = dx**2 + dy**2 + dz**2 - (r1 + r2)**2
    
    det = B**2 - (4 * A * C)
    if det < 0 or A == 0:
        print('No collision')
        continue
    
    t1 = (-B - sqrt(det)) / (2*A)
    t2 = (-B + sqrt(det)) / (2*A)
    if t1 > 0:
        print(round(t1, 3))
    elif t2 > 0:
        print(round(t2, 3))
    else:
        print('No collision')