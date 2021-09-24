k, n = int(input()), int(input())
time = 0
for _ in range(n):
    t, z = input().split()
    if time < 210 and time + int(t) >= 210:
        print(k)
    time += int(t)
    if z == 'T':
        k = (k % 8) + 1