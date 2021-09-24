line = input()
while line != "0":
    F, R = tuple(map(int, line.split()))
    f = list(map(int, input().split()))
    r = list(map(int, input().split()))
    ratios = []
    for t1 in f:
        for t2 in r:
            ratios.append(t2/t1)
    ratios = sorted(ratios)
    maxSpread = 0
    for i in range(len(ratios) - 1):
        maxSpread = max(maxSpread, ratios[i+1]/ratios[i])
    print("%.2f" % maxSpread)
    line = input()