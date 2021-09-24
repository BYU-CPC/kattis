from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x))
    stdout.write(end)

l, d, x = map(int, [_i() for _ in range(3)])

def calc_sum(num):
    return num if num < 10 else (num % 10 + calc_sum(num//10))

m, n = d, l
while calc_sum(n) != x: n += 1
while calc_sum(m) != x: m -= 1
_p(n)
_p(m)

stdout.flush()