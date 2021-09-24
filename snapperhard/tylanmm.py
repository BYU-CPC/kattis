for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    k %= 2**n
    if k == (1 << n) - 1:
        print(f'Case #{t}: ON')
    else:
        print(f'Case #{t}: OFF')