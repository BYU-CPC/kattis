n, temps = int(input()), list(map(int, input().split()))
lo, loI = max(temps[0], temps[2]), 0
for i in range(1, n-2):
    hi = max(temps[i], temps[i+2])
    if hi < lo:
        lo = hi
        loI = i
print(loI+1, lo)