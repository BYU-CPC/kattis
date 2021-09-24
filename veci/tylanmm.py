from itertools import permutations

x = tuple(input())
digits = sorted(x)
for n in permutations(digits):
    if n > x:
        print(''.join(n))
        break
else:
    print(0)