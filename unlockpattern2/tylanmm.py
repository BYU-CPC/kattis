def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])
    if val < 0:
        return 1    # counter clockwise
    elif val > 0:
        return -1   # clockwise
    else:
        return 0    # colinear

# cartesian coordinates for each number
nums = [0] + [(i, j) for j in range(2, -1, -1) for i in range(3)]

# pre-classify every combination of 3 numbers (9*8*7 = 504)
dir = [[['' for _ in range(10)] for _ in range(10)] for _ in range(10)]
for i in range(1, 10):
    prev = nums[i]
    for j in range(1, 10):
        if i == j: continue
        curr = nums[j]
        for k in range(1, 10):
            if i == k or j == k: continue
            o = orientation(prev, curr, nums[k])
            if o == 1:
                dir[i][j][k] = 'L'
            elif o == -1:
                dir[i][j][k] = 'R'
            elif (prev[0] - curr[0] == curr[0] - nums[k][0]) and (prev[1] - curr[1] == curr[1] - nums[k][1]):
                dir[i][j][k] = 'S'
            else:
                dir[i][j][k] = 'A'

# explicitly state which unvisited numbers would block a certain connection
blocks = [[0]*10 for _ in range(10)]
blocks[1][3] = 2
blocks[1][7] = 4
blocks[1][9] = 5
blocks[2][8] = 5
blocks[3][1] = 2
blocks[3][7] = 5
blocks[3][9] = 6
blocks[4][6] = 5
blocks[6][4] = 5
blocks[7][1] = 4
blocks[7][3] = 5
blocks[7][9] = 8
blocks[8][2] = 5
blocks[9][1] = 5
blocks[9][3] = 6
blocks[9][7] = 8

# recursively build up an unlock pattern
seq = input()
used = [False]*10
used[0] = True
ways = 0
def solve(i, j, index):
    if index == 7:
        global ways
        ways += 1
        return

    for k in range(1, 10):
        if not used[k] and used[blocks[j][k]] and (seq[index] == '?' or dir[i][j][k] == seq[index]):
            used[k] = True
            solve(j, k, index+1)
            used[k] = False
        
    used[j] = False

# run through every possible starting combination
for i in range(1, 10):
    for j in range(1, 10):
        if i == j or not used[blocks[i][j]]: continue
        used[i] = used[j] = True
        solve(i, j, 0)
        used[i] = used[j] = False

print(ways)