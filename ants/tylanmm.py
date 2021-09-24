import sys
t = int(input())
nums = list(map(int, sys.stdin.read().split()))
i = 0
while i < len(nums):
    l, n = nums[i], nums[i+1]
    i += 2
    lo, hi = 0, 0
    for j in range(i, i+n):
        lo = max(lo, min(nums[j], l - nums[j]))
        hi = max(hi, max(nums[j], l - nums[j]))
    print(lo, hi)
    i += n