n, m = tuple(map(int, input().split()))

freq = {}
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i + j) not in freq:
            freq[i+j] = 1
        else:
            freq[i+j] += 1

best = max(list(freq.values()))
for f in freq:
    if freq[f] == best:
        print(f)