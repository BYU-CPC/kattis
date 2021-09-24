n, l, p = map(int, input().split())
car = [0]*n
hi = 0
for _ in range(p):
    loc = int(input())
    c = min((loc + l) // l - 1, n-1)
    car[c] += 1
    hi = max(hi, abs(c*l + l//2 - loc))
    
print(hi)
print(max(car))