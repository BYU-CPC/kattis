from sys import stdin

def solve(nums):
    canMake = [False]*(nums[-1]+1)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if canMake[nums[j] - nums[i]]:
                print('not a ruler')
                return
            canMake[nums[j] - nums[i]] = True
    missing = [str(i) for i in range(1, len(canMake)) if not canMake[i]]
    if missing:
        print(f'missing {" ".join(missing)}')
    else:
        print('perfect')

for line in stdin.readlines():
    nums = sorted(list(map(int, line.split())))
    solve(nums)