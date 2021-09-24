R, C = map(int, input().split())
r, c = 0, 0
grid = [input() for _ in range(R)]
seen = set()
while -1 < r < R and -1 < c < C:
    if (r, c) in seen:
        print('Lost')
        break
    seen.add((r, c))
    
    if   grid[r][c] == 'N': r -= 1
    elif grid[r][c] == 'S': r += 1
    elif grid[r][c] == 'W': c -= 1
    elif grid[r][c] == 'E': c += 1
    else:
        print(len(seen)-1)
        break
else:
    print('Out')