N, t = tuple(map(int, input().split()))
A = sorted(list(map(int, input().split())))

if t == 1:
    i = 0
    j = N - 1
    while i < j:
        if A[i] + A[j] < 7777:
            i += 1
        elif A[i] + A[j] > 7777:
            j -= 1
        else:
            print("Yes")
            break
    if A[i] + A[j] != 7777:
        print("No")

elif t == 2:
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("Contains duplicate")
            break
    else:
        print("Unique")

elif t == 3:
    freq = {}
    for a in A:
        if a not in freq:
            freq[a] = 1
        else:
            freq[a] += 1
        if freq[a] > N/2:
            print(a)
            break
    else:
        print(-1)

elif t == 4:
    if N % 2 == 1:
        print(A[N//2])
    else:
        print(A[N//2 - 1], A[N//2])

else:
    for a in A:
        if a >= 100:
            if a > 999:
                break
            print(a, end=' ')