grid = [input() for _ in range(4)]
total = 0
for a in range(4):
    for b in range(4):
        if grid[a][b] == '.':
            continue
        i = ord(grid[a][b]) - ord('A')
        c, d = i // 4, i % 4
        total += abs(a - c) + abs(b - d)
print(total)