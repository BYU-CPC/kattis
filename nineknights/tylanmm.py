grid = [input() for _ in range(5)]
dirs = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
def solve():
    for i in range(5):
        for j in range(5):
            if grid[i][j] != 'k': continue
            for di, dj in dirs:
                if 0 <= i + di < 5 and 0 <= j + dj < 5 and grid[i+di][j+dj] == 'k':
                    return 'invalid'
    return 'valid' if ''.join(grid).count('k') == 9 else 'invalid'
print(solve())