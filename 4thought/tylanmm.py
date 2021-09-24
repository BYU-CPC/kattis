vals = {}
ops = ['*', '//', '+', '-']
for o1 in ops:
    for o2 in ops:
        for o3 in ops:
            vals[eval(f'4 {o1} 4 {o2} 4 {o3} 4')] = (o1, o2, o3)

for _ in range(int(input())):
    n = int(input())
    if n in vals:
        o1, o2, o3 = vals[n]
        o1 = '/' if o1 == '//' else o1
        o2 = '/' if o2 == '//' else o2
        o3 = '/' if o3 == '//' else o3
        print(f'4 {o1} 4 {o2} 4 {o3} 4 = {n}')
    else:
        print('no solution')