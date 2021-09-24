from sys import stdin, stdout

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

line = _i().split()
h = int(line[0])
top = 2**(h+1)
if len(line) == 1:
    _p(top - 1)
else:
    path = line[1]
    i = 1
    for j in range(len(path)):
        if path[j] == 'L':
            i = i*2
        else:
            i = i*2 + 1
    _p(top - i)

stdout.flush()