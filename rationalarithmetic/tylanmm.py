from sys import stdin, stdout, setrecursionlimit
from math import gcd

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

def evalfrac(n1, d1, n2, d2, op):
    n, d = None, None

    if op == '+':
        n1, n2 = n1*d2, n2*d1
        n, d = n1+n2, d1*d2
    elif op == '-':
        n1, n2 = n1*d2, n2*d1
        n, d = n1-n2, d1*d2
    elif op == '/':
        n, d = n1*d2, d1*n2
    else: # op == '*':
        n, d = n1*n2, d1*d2
    
    # reduce
    gcf = gcd(n, d)
    return n//gcf, d//gcf

for _ in range(int(_i())):
    n1, d1, op, n2, d2 = _i().split()
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)
    num, den = evalfrac(n1, d1, n2, d2, op)
    if den < 0:
        num, den = num * -1, den * -1
    _p(f'{num} / {den}')

stdout.flush()