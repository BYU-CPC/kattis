n, m = input(), input()
res = []
if len(m)-1 < len(n):
    res = list(n[:-len(m)+1]) + ['.'] + list(n[-len(m)+1:])
else:
    res = ['0.'] + ['0']*(len(m)-len(n)-1) + list(n)

while res[-1] == '0':
    res.pop()
if res[-1] == '.':
    res.pop()

print(''.join(res))