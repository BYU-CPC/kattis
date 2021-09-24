for _ in range(int(input())):
    k, n = map(int, input().split())
    print(k, n + n*(n+1)//2)