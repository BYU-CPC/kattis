import sys

def binSearch(n, nums):
    lo, hi = 0, len(nums)-1
    ans = nums[hi]
    while lo <= hi:
        mid = (lo + hi)//2
        if nums[mid] == n:
            return n
        elif nums[mid] > n:
            ans = nums[mid] if abs(n - ans) > abs(n - nums[mid]) else ans
            hi = mid - 1
        else:
            ans = nums[mid] if abs(n - ans) > abs(n - nums[mid]) else ans
            lo = mid + 1
    return ans

def solve(n, nums, m, queries):
    sums = []
    for i in range(n):
        for j in range(i+1, n):
            sums.append(nums[i] + nums[j])
    sums.sort()
    
    res = []
    for q in queries:
        res.append((q, binSearch(q, sums)))
    return res

raw, i, t = [int(n) for n in sys.stdin.readlines()], 0, 1
while i < len(raw):
    # read the values
    n = raw[i]
    i += 1
    nums = raw[i:i+n]
    i += n
    m = raw[i]
    i += 1
    queries = raw[i:i+m]
    i += m

    res = solve(n, nums, m, queries)
    print(f'Case {t}:')
    for s, c in res:
        print(f'Closest sum to {s} is {c}.')
    t += 1