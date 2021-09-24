for _ in range(int(input())):
    group = list(map(int, input().split()))
    g, group = group[0], group[1:]
    for i in range(1, g-1):
        if group[i] != group[i-1] + 1:
            print(i+1)
            break