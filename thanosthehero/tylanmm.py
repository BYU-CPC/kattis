n = int(input())
worlds = list(map(int, input().split()))
kill = 0
for i in range(2, n+1):
    if worlds[-i] >= worlds[1-i]:
        if worlds[1-i] == 0:
            print(1)
            break
        kill += worlds[-i] - worlds[1-i] + 1
        worlds[-i] = worlds[1-i] - 1
else:
    print(kill)