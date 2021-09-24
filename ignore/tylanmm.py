from sys import stdin

digit = ['0', '1', '2', '5', '9', '8', '6']
for k in map(int, stdin.readlines()):
    ans = ''
    while k:
        ans += digit[k % 7]
        k //= 7
    print(ans)