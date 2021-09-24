for _ in range(int(input())):
    n = int(input())
    hi, hiG = -1, 0
    for g in range(1, n+1):
        a, b, c = map(int, input().split())
        torque = b*b/(4*a) + c
        if torque > hi:
            hi = torque
            hiG = g
    print(hiG)