from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
while n and m:
    jack = {int(stdin.readline()) for _ in range(n)}
    jill = {int(stdin.readline()) for _ in range(m)}
    stdout.write(str(len(jack.intersection(jill))))
    stdout.write('\n')
    n, m = map(int, stdin.readline().split())
stdout.flush()