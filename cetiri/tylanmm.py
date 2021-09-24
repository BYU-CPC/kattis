nums = sorted(list(map(int, input().split())))
d = min(nums[1] - nums[0], nums[2] - nums[1])
if nums[2] == nums[0] + 2*d:
    print(nums[2] + d)
elif nums[2] == nums[1] + 2*d:
    print(nums[1] + d)
else:
    print(nums[0] + d)