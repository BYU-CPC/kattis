N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    print(7)

elif t == 2:
    if A[0] > A[1]:
        print('Bigger')
    elif A[0] == A[1]:
        print('Equal')
    else:
        print('Smaller')

elif t == 3:
    print(sorted([A[0], A[1], A[2]])[1])

elif t == 4:
    print(sum(A))

elif t == 5:
    total = 0
    for n in A:
        total += 0 if n % 2 else n
    print(total)

elif t == 6:
    for i in range(N):
        A[i] = chr((A[i] % 26) + 97)
    print(''.join(A))

else:
    seen = {0}
    i = 0
    while True:
        i = A[i]
        if i > N-1:
            print('Out')
            break
        elif i == N-1:
            print('Done')
            break
        elif i in seen:
            print('Cyclic')
            break
        seen.add(i)