def sumDigits(num):
    total = 0
    while num:
        total += num%10
        num //= 10
    return total

n = int(input())
while n:
    digitSum = sumDigits(n)
    p = 11
    total = sumDigits(p*n)
    while total != digitSum:
        p += 1
        total = sumDigits(p*n)
    print(p)
    
    n = int(input())