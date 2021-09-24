from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

n, m, l = map(int, _i().split())
folds = [0]
folds.extend(list(map(int, _i().split())))
cuts = list(map(int, _i().split()))

inc = [[0, 1]]
dist = 0
for i in range(1, n+1):
    folds[i] = (l - folds[i]) - dist
    dist += folds[i]
    if i % 2:
        inc.append([inc[-1][0] + folds[i], -2])
    else:
        inc.append([inc[-1][0] - folds[i], 2])

if n % 2:
    inc.append([inc[-1][0] - (l - dist), 1])
else:
    inc.append([inc[-1][0] + (l - dist), -1])

inc.sort()

amt = [inc[0]]
for i in range(1, n+2):
    if inc[i][0] == amt[-1][0]:
        amt[-1][1] += inc[i][1]
    else:
        amt.append(list(inc[i]))

for i in range(1, len(amt)):
    amt[i][1] += amt[i-1][1]

newAmt = [amt[0]]
for i in range(1, len(amt)):
    if amt[i][1] != newAmt[-1][1]:
        newAmt.append(amt[i])
amt = newAmt

cuts.append(int(1e18) + 1)
total = 0
i = 0
last = amt[0][0]
lastLayers = 0
for c in cuts:
    while i < len(amt) and amt[i][0] <= c:
        total += (amt[i][0] - last) * lastLayers
        last = amt[i][0]
        lastLayers = amt[i][1]
        i += 1
    total += (c - last) * lastLayers
    last = c
    _p(total, ' ')
    total = 0

stdout.flush()