n = int(input())
while n:
    times = []
    for _ in range(n):
        line = input()
        t, z = line.split()
        h, m = t.split(':')
        times.append((int(h), int(m), z))

    def time(t):
        return t[1] + (t[0] % 12)*60 + (12*60 if t[2] == 'p.m.' else 0)

    times.sort(key=time)
    for h, m, z in times:
        print(f'{h}:{m:02d} {z}')
    print()
    n = int(input())