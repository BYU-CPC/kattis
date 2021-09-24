n = int(input())
match = {')': '(', '}': '{', ']': '['}
s = []
l = input()
for i in range(n):
    if l[i] == ' ': continue
    if l[i] not in match: s.append(l[i])
    else:
        if len(s) == 0 or s.pop() != match[l[i]]:
            print(l[i], i)
            break
else:
    print('ok so far')
