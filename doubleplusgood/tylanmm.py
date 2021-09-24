nums = input().split('+')
lim = len(nums) - 1

subs = []
def makeSubset(subset, i):
    if i == lim:
        subset.reverse()
        subs.append(subset)
        return
    makeSubset(subset.copy(), i + 1)
    subset.append(i)
    makeSubset(subset.copy(), i + 1)

makeSubset([], 0)

possNums = set()
for s in subs:
    newNums = nums.copy()
    for p in s:
        num = newNums[p] + newNums[p+1]
        newNums.pop(p+1)
        newNums[p] = num
    possNums.add(sum(list(map(int, newNums))))

print(len(possNums))

# recursion