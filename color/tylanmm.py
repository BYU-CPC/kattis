S, C, K = map(int, input().split())
sock = sorted(map(int, input().split()))

lo, load, amt = sock[0], 1, 1
for s in sock[1:]:
    if s - lo > K or load+1 > C:
        lo, load = s, 0
        amt += 1
    load += 1
print(amt)