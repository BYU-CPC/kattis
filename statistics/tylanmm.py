import sys
i = 1
for line in sys.stdin.readlines():
    line = list(map(int, line.split()))[1:]
    lo, hi = min(line), max(line)
    print(f'Case {i}: {lo} {hi} {hi-lo}')
    i += 1