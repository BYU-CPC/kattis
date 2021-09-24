import sys
for line in sys.stdin.readlines():
    m, p, l, e, r, s, n = map(int, line.split())
    for _ in range(n):
        m, p, l = p//s, l//r, e*m
    print(m)