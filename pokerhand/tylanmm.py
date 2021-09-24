hand = input().split()
freq = {c[0]:0 for c in hand}
for c in hand:
    freq[c[0]] += 1
print(max(freq.values()))