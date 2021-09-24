vals = ['', 'single', 'double', 'triple']
def solve(n):
    for a in range(1, 21):
        for b in range(1, 21):
            for c in range(1, 21):
                for i in range(1, 4):
                    for j in range(4):
                        for k in range(4):
                            if a*i + b*j + c*k == n:
                                print(f'{vals[i]} {a}')
                                if j: print(f'{vals[j]} {b}')
                                if k: print(f'{vals[k]} {c}')
                                return
    print('impossible')

solve(int(input()))