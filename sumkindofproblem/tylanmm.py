for _ in range(int(input())):
    k, n = map(int, input().split())
    total = n * (n+1) // 2
    oSum = (1 + (n-1))*n
    eSum = (2 + (n-1))*n
    print(f'{k} {total} {oSum} {eSum}')