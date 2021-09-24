for _ in range(int(input())):
    turts = list(map(int, input().split()))
    total = 0
    for i in range(1, len(turts)-1):
        total += max(0, turts[i] - 2*turts[i-1])
    print(total)