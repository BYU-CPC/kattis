from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

CHARS = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./  '
map = {}
for i, c in enumerate(CHARS):
    map[c] = i-1

for line in stdin:
    line = list(line.strip())

    for i, c in enumerate(line):
        line[i] = CHARS[map[c]]

    _p(''.join(line))

stdout.flush()