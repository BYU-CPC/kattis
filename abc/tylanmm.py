nums = sorted(list(map(int, input().split())))
order = input()
print(' '.join(map(str, [nums[ord(order[0])-65], nums[ord(order[1])-65], nums[ord(order[2])-65]])))