import sys
for line in sys.stdin.readlines():
    total = 0
    for c in line.strip():
        num = ord(c)
        for _ in range(7):
            total ^= 1 << (num & 1)
            num >>= 1
    print('trapped' if total else 'free')