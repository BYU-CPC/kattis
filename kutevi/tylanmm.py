n, k = map(int, input().split())
mirko = list(map(int, input().split()))
slavko = list(map(int, input().split()))

canMake = [False]*361
angles = {0}
newAngle = True
while newAngle:
    newAngle = False
    newAngles = set()
    for angle in angles:
        for a in mirko:
            angleA, angleB = (angle-a)%360, (angle+a)%360
            if not canMake[angleA] or not canMake[360 - angleA]:
                newAngle = True
                canMake[angleA] = True
                canMake[360 - angleA] = True
                newAngles.add(angleA)
                newAngles.add(360 - angleA)

            if not canMake[angleB] or not canMake[360 - angleB]:
                newAngle = True
                canMake[angleB] = True
                canMake[360 - angleB] = True
                newAngles.add(angleB)
                newAngles.add(360 - angleB)
    angles |= newAngles

for angle in slavko:
    print('YES' if canMake[angle] else 'NO')