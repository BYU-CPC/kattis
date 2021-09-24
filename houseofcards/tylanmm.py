n = int(input())
res = n % 8
if res == 0 or res == 5:
    print(n)
elif res < 5:
    print(n+5-res)
else:
    print(n+3-(res-5))