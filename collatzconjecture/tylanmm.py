from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

steps = {1: 0}

def collatz(n):
    if n not in steps:
        steps[n] = collatz((3*n+1) if n%2 else (n//2)) + 1
    return steps[n]

a, b = map(int, _i().split())
while a and b:
    s1, s2 = collatz(a), collatz(b)
    
    # get them to the same height in the tree
    aCopy, bCopy = a, b
    while s1 > s2:
        aCopy = (3*aCopy+1) if aCopy%2 else (aCopy//2)
        s1 -= 1
    while s2 > s1:
        bCopy = (3*bCopy+1) if bCopy%2 else (bCopy//2)
        s2 -= 1
    
    # find LCA
    while aCopy != bCopy:
        aCopy = (3*aCopy+1) if aCopy%2 else (aCopy//2)
        bCopy = (3*bCopy+1) if bCopy%2 else (bCopy//2)
        s1 -= 1
        s2 -= 1
    
    # output
    _p(f'{a} needs {steps[a] - s1} steps, {b} needs {steps[b] - s2} steps, they meet at {aCopy}')

    a, b = map(int, _i().split())

stdout.flush()