from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

def calc(x, y):
    det = ((4*x + 4*y)**2 - 48*x*y)**0.5
    h1, h2 = (4*x + 4*y + det) / 24, (4*x + 4*y - det) / 24
    return max((x - 2*h1) * (y - 2*h1) * h1, (x - 2*h2) * (y - 2*h2) * h2)

# (x - 2h) * (y - 2h) * h = V
# (xy - 2hx - 2hy + 4h^2) * h = V
# 4h^3 - h^2(2x + 2y) + hxy = V
# 12h^2 - 2h(2x + 2y) + xy = dV/dh
# h = (4x + 4y +/- sqrt((4x + 4y)**2 - 48xy)) / 24

for _ in range(int(_i())):
    x, y = map(int, _i().split())
    _p(calc(x, y))

stdout.flush()