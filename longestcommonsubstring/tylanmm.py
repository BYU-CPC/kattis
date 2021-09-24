n = int(input())
S = [input() for _ in range(n)]
S.sort(key=len)

def check(length):
    if length == 0 or n == 1: return True
    for i in range(len(S[0])-length+1):
        sub = S[0][i:i+length]
        if sub in S[1]:
            for s in S[2:]:
                if sub not in s:
                    break
            else:
                return True
    return False

lo, hi = 0, len(S[0])
while lo <= hi:
    mid = (lo + hi)//2
    if check(mid):
        lo = mid + 1
    else:
        hi = mid - 1
print(hi)