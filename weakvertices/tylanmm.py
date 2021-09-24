n = int(input())
while n != -1:
    mat = [list(map(int, input().split())) for _ in range(n)]
    weakV = set()
    for i in range(n):
        weak = True
        for j in range(n):
            if i == j or not mat[i][j]: continue
            for k in range(n):
                if j == k or not mat[j][k]: continue
                if mat[i][k]:
                    weak = False
                    break
            if not weak:
                break
        if weak:
            weakV.add(i)

    print(' '.join(map(str, sorted(list(weakV)))))
    
    n = int(input())