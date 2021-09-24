days = [False] * 366
for _ in range(int(input())):
    s, t = map(int, input().split())
    for i in range(s, t+1):
        days[i] = True
print(sum(days))