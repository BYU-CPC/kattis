n, bytes = int(input()), list(map(int, input().split()))
res = [0]*256
for i in range(256):
    res[i ^ (((i << 1) | (1 << 8)) - (1 << 8))] = i
print(' '.join([str(res[b]) for b in bytes]))