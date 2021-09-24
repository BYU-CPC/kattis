pieces = {1:[[0], [0, 0, 0, 0]], 2:[[0, 0]], 3:[[0, 0, 1], [1, 0]], 4:[[1, 0, 0], [0, 1]], 5:[[0, 0, 0], [0, 1], [1, 0, 1], [1, 0]], 6:[[0, 0, 0], [0, 0], [0, 1, 1], [2, 0]], 7:[[0, 0, 0], [0, 2], [1, 1, 0], [0, 0]]}

c, p = map(int, input().split())
heights = list(map(int, input().split()))
count = 0
for dir in pieces[p]:
    for i in range(c - len(dir) + 1):
        for j in range(1, len(dir)):
            if heights[i+j]-dir[j] != heights[i+j-1] - dir[j-1]:
                break
        else:
            count += 1
print(count)