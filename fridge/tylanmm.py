from collections import Counter

freq = Counter({i: 0 for i in range(10)})
freq.update(Counter(map(int, input())))
freq[10] = freq[0]
freq.pop(0)

if 0 in freq.values():
    none = sorted([x for x in freq if freq[x] == 0])
    print(none[0])
else:
    order = sorted(list(range(1, 11)), key=lambda x: freq[x])
    if order[0] != 10:
        print(str(order[0]) * (freq[order[0]] + 1))
    else:
        print('1' + ('0' * (freq[10] + 1)))