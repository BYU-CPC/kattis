for _ in range(int(input())):
    n = int(input())
    print(len({input() for _ in range(n)}))