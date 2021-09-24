n = int(input())
while n != -1:
    miles = 0
    time = 0
    for _ in range(n):
        s, t = map(int, input().split())
        miles += s * (t - time)
        time = t
    print("%d miles" % miles)
    n = int(input())