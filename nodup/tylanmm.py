from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

phrase = _i().split()
_p('yes' if len(phrase) == len(set(phrase)) else 'no')

stdout.flush()