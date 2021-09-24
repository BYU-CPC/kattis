from sys import stdin, stdout

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n = int(_i())
points = []
xs = [0]*100001
ys = [0]*100001
for _ in range(n):
    x, y = map(int, _i().split())
    xs[x] += 1
    ys[y] += 1
    points.append((x, y))

total = 0
for x, y in points:
    total += (xs[x] - 1) * (ys[y] - 1)
_p(total)

stdout.flush()