for _ in range(int(input())):
    x = int(input())
    hi = 0
    for i in range(len(str(x))):
        xi = int(str(x)[:i+1])
        total = 0
        while xi:
            total += xi & 1
            xi >>= 1
        hi = max(hi, total)
    print(hi)