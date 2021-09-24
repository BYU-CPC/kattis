p, d = map(int, input().split())
districts = {i:[0, 0] for i in range(1, d+1)}
for _ in range(p):
    i, a, b = map(int, input().split())
    districts[i][0] += a
    districts[i][1] += b

voteA, voteB = 0, 0
wasteA, wasteB = 0, 0
for d in districts:
    a, b = districts[d]
    voteA += a
    voteB += b
    if a > b:
        print('A', a - ((a+b)//2 + 1), b)
        wasteA += a - ((a+b)//2 + 1)
        wasteB += b
    else:
        print('B', a, b - ((a+b)//2 + 1))
        wasteA += a
        wasteB += b - ((a+b)//2 + 1)

print(abs(wasteA - wasteB) / (voteA + voteB))