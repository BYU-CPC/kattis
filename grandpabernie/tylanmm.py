n = int(input())
trip = {}
for _ in range(n):
    s, y = input().split()
    y = int(y)
    if s not in trip:
        trip[s] = [y]
    else:
        trip[s].append(y)

for s in trip:
    trip[s].sort()

for _ in range(int(input())):
    s, k = input().split()
    k = int(k) - 1
    print(trip[s][k])