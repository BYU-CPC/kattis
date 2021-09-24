r, b = map(int, input().split())
total = r+b
for l in range(2, int(total**0.5) + 1):
    if total % l == 0:
        w = total // l
        if 2*(l + w) - 4 != r: continue
        if (l - 2) * (w - 2) != b: continue
        print(max(l, w), min(l, w))
        break

'''
LW = R + B
2(L + W) - 4 = R
(L - 1)(W - 1) = B
'''