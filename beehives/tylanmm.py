import math

def calcDist(hive1, hive2):
    return math.sqrt(abs(hive1[0]-hive2[0])**2 + abs(hive1[1]-hive2[1])**2)

line = input().split()
while line != ["0.0", "0"]:
    d = float(line[0])
    n = int(line[1])
    hives = []
    for i in range(n):
        hives.append(tuple(map(float, input().split())))
    sour = set()
    sweet = set()
    for i in range(len(hives)):
        for j in range(len(hives)):
            if i != j:
                if d >= calcDist(hives[i], hives[j]):
                    sour.add(hives[i])
                    sour.add(hives[j])
                    break
        if hives[i] not in sour:
            sweet.add(hives[i])
    print("%d sour, %d sweet" % (len(sour), len(sweet)))
    line = input().split()