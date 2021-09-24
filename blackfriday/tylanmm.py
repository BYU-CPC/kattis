n = int(input())
freq = {}
rolls = list(map(int, input().split()))
for n in rolls:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1
hi = 0
for n in freq:
    if freq[n] == 1:
        hi = max(hi, n)
if hi:
    print(rolls.index(hi)+1)
else:
    print('none')