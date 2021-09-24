for _ in range(int(input())):
    n = int(input())
    dvds = map(int, input().split())
    curr = 0
    for disk in dvds:
        if disk == curr+1:
            curr += 1
    print(n - curr)