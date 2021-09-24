for t in range(int(input())):
    n, A, B, C, D, x, y, M = map(int, input().split())
    trees = [(x, y)]
    for i in range(n-1):
        x = (A*x + B) % M
        y = (C*y + D) % M
        trees.append((x, y))
    
    count = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                x, y = (trees[i][0] + trees[j][0] + trees[k][0])/3, (trees[i][1] + trees[j][1] + trees[k][1])/3
                if int(x) == x and int(y) == y:
                    count += 1
    
    print(f'Case #{t+1}: {count}')