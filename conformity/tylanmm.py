n = int(input())
frosh = {}
for _ in range(n):
    f = ' '.join(sorted(input().split()))
    if f in frosh:
        frosh[f] += 1
    else:
        frosh[f] = 1

m = max(frosh.values())
print(m * list(frosh.values()).count(m))