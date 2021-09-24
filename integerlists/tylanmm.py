from sys import stdin, stdout
from collections import deque

lines = stdin.readlines()
t = int(lines[0])
i = 1
for _ in range(t):
    prog = lines[i].strip()
    n = int(lines[i+1])
    nums = deque(lines[i+2][1:-2].split(','))
    
    dir = 0
    for com in prog:
        if com == 'R':
            dir ^= 1
        elif len(nums) == 1 and nums[0] == '':
            stdout.write('error\n')
            break
        elif nums:
            if dir:
                nums.pop()
            else:
                nums.popleft()
        else:
            stdout.write('error\n')
            break
    else:
        if dir:
            nums = list(nums)[::-1]
        stdout.write('[' + ','.join(nums) + ']\n')
    
    i += 3

stdout.flush()