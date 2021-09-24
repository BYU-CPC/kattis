secs = [False]*(24*60*60)
jobs = 0

def evaluate(t):
    res = []
    for n in t:
        if '-' in n:
            start, end = map(int, n.split('-'))
            for i in range(start, end+1):
                res.append(int(i))
        elif n == '*':
            res.append('*')
        else:
            res.append(int(n))
    return res

for _ in range(int(input())):
    h, m, s = map(lambda x: evaluate(x.split(',')), input().split())
    if h[0] == '*':
        h = list(range(24))
    if m[0] == '*':
        m = list(range(60))
    if s[0] == '*':
        s = list(range(60))
    jobs += len(h) * len(m) * len(s)
    for H in h:
        for M in m:
            for S in s:
                secs[H*3600 + M*60 + S] = True

print(sum(secs), jobs)