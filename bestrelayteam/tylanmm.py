n = int(input())
runners = []
for _ in range(n):
    name, leg1, legs = input().split()
    leg1 = float(leg1)
    legs = float(legs)
    runners.append((name, leg1, legs))

top = sorted(runners, key=lambda x: x[2])[:4]
runners.sort(key=lambda x: x[1])
lo = float('inf')
best = []
for r in runners[:4]:
    if r not in top:
        if lo > sum([run[2] for run in top[:3]]) + r[1]:
            lo = sum([run[2] for run in top[:3]]) + r[1]
            best = [r[0]] + [run[0] for run in top[:3]]
    else:
        if lo > sum([run[2] for run in top]) - r[2] + r[1]:
            lo = sum([run[2] for run in top]) - r[2] + r[1]
            best = [r[0]] + [run[0] for run in top if run != r]

print(lo)
print('\n'.join(best))