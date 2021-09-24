line = input()
while line != '0':
    n, *perm = list(map(int, line.split()))
    s = list(input())
    while len(s) % n:
        s.append(' ')

    res = ['']*len(s)
    for i in range(0, len(s), n):
        for j in range(n):
            res[i+j] = s[i+perm[j]-1]
    print('\'' + ''.join(res) + '\'')

    line = input()