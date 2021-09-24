from sys import stdin

for line in stdin.readlines():
    nums = list(map(int, line.split()))
    total = sum(nums)
    for n in nums:
        if n == total - n:
            print(n)
            break