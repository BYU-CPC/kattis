n, nums = int(input()), input().split()
for i in range(n):
    if nums[i].isdigit():
        if int(nums[i]) != i+1:
            print('something is fishy')
            break
else:
    print('makes sense')