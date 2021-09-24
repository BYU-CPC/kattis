n, junk = int(input()), list(map(int, input().split()))
lo, loI = junk[0], 0
for i in range(n):
    if junk[i] < lo:
        lo, loI = junk[i], i
print(loI)