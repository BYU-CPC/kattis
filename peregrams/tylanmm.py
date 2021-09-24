w = input()
freqs = {}
for c in w:
    if c in freqs:
        freqs[c] += 1
    else:
        freqs[c] = 1

odd = 0
for c in freqs:
    if freqs[c] % 2 == 1:
        odd += 1

if odd > 1:
    print(odd - 1)
else:
    print(0)