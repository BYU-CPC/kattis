group = [[0]*4 for _ in range(2)]
for _ in range(int(input())):
    g, a, b, c = map(lambda x: 1 if x == 'Y' else 0, input())
    group[g][0] += 1
    group[g][1] += a
    group[g][2] += b
    group[g][3] += c

for i in range(1, 4):
    control = group[0][i] / group[0][0]
    test = group[1][i] / group[1][0]
    if test >= control:
        print('Not Effective')
    else:
        print((1 - test / control) * 100)