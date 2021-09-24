from collections import Counter

n = int(input())
total = Counter([input() for _ in range(n)])
m = min(total.values())
res = []
for costume in total:
    if total[costume] == m:
        res.append(costume)
print('\n'.join(sorted(res)))