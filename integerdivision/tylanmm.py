from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

n, d = map(int, _i().split())
nums = sorted(map(int, _i().split()))

i, j = 0, 1
ans = 0
while j < n:
    while j < n:
        div1, div2 = nums[i] // d, nums[j] // d
        if div1 != div2:
            break
        j += 1
    ans += (j - i - 1) * (j - i) // 2
    i, j = j, j + 1

_p(ans)

stdout.flush()

# Sorting, two pointer