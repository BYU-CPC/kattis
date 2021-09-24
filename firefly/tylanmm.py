from sys import stdin, stdout

n, h = map(int, stdin.readline().split())
num = [n//2] + [0]*(h-1) + [-n//2]
for _ in range(n//2):
    num[int(stdin.readline())] -= 1
    num[~int(stdin.readline())] += 1

lo = num[0]
amt = 1
for i in range(1, h):
    num[i] += num[i-1]
    if num[i] < lo:
        lo = num[i]
        amt = 1
    elif num[i] == lo:
        amt += 1

stdout.write('%d %d\n' % (lo, amt))
stdout.flush()