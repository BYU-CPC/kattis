n, y = tuple(map(int, input().split()))
obs = sorted(list(set([int(input()) for _ in range(y)])))
obI = 0
count = 0
while count < n:
    if obI >= len(obs) or count != obs[obI]:
        print(count)
    else:
        obI += 1
    count += 1
print("Mario got %d of the dangerous obstacles." % (len(obs)))