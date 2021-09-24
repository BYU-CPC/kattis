a = [int(input()) for _ in range(int(input()))]
l, r = 0, sum(a)
hi = 0
for an in a:
    r -= an
    l += an*an
    hi = max(hi, l*r)
print(hi)