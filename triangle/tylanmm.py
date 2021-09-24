import sys
i = 0
for n in sys.stdin.readlines():
    n = int(n)
    i += 1
    print(f'Case {i}: {len(str(3**(n+1) // 2**n))}')