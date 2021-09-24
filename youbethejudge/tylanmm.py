from sys import stdin

def isPrime(num):
    if num == 2: return True
    for n in range(2, int(num**0.5)+1):
        if num % n == 0:
            return False
    return True

def isValid(num):
    try:
        n = int(num)
        if n <= 1 or n > 1e9:
            return False
        if num[0] in '+0':
            return False
        return True
    except:
        return False

def solve():
    nums = stdin.read().strip().split()
    if len(nums) != 3:
        return False
    
    if not all([isValid(num) for num in nums]):
        return False
    
    nums = [int(num) for num in nums]
    if 3 < nums[0] and nums[0] % 2 == 0 and nums[1] + nums[2] == nums[0] and isPrime(nums[1]) and isPrime(nums[2]):
        return True
    
    return False
    
print(1 if solve() else 0)