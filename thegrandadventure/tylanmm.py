match = {'b': '$', 't': '|', 'j': '*'}
for _ in range(int(input())):
    s = []
    for c in input():
        if c in '$|*':
            s.append(c)
        elif c in 'btj':
            while s and s[-1] != match[c]:
                s.pop()
            if len(s) == 0 or s[-1] != match[c]:
                print('NO')
                break
            s.pop()
    else:
        print('NO' if s else 'YES')