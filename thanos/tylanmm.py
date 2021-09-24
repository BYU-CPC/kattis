for _ in range(int(input())):
    p, r, f = map(int, input().split())
    years = 0
    while p <= f:
        p *= r
        years += 1
    print(years)