from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

n = int(_i())
teams = [_i().split() for _ in range(n)]
awarded = set()
i = 0
while len(awarded) < 12:
    if teams[i][0] not in awarded:
        awarded.add(teams[i][0])
        _p(f'{teams[i][0]} {teams[i][1]}')
    i += 1

stdout.flush()