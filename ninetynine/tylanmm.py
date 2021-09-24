amt = 1
n = 1
print(n)
while n < 99:
    n = int(input())
    if n % 3:
        n += 3 - (n % 3)
    else:
        amt ^= 1
        n += amt + 1
    print(n)