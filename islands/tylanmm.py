for t in range(1, int(input())+1):
    data = list(map(int, input().split()))[1:]
    islands = 0
    for i in range(1, 11):
        for j in range(i, 11):
            if data[i-1] >= data[i] or data[j] <= data[j+1] or data[i] <= data[j+1] or data[i-1] >= data[j]:
                continue
            level = max(data[i-1], data[j+1])
            for k in range(i+1, j):
                if data[k] <= level:
                    break
            else:
                islands += 1
    print(t, islands)