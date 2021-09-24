for _ in range(int(input())):
    K, n, m, k = map(int, input().split())
    good = set(range(1, n+1))
    for i in range(m, n+1, k):
        good.discard(i)
    
    ans = [0]*(n+1)
    ans[0] = 1
    for i in range(1, n+1):
        for num in good:
            if i - num >= 0:
                ans[i] += ans[i-num]
    print(K, ans[-1])