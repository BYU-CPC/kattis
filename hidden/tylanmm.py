p, s = input().split()
i = 0
for c in s:
    if i < len(p) and p[i] == c:
        i += 1
    elif i == len(p):
        continue
    elif c in p[i:]:
        print('FAIL')
        break
else:
    print('PASS' if i == len(p) else 'FAIL')