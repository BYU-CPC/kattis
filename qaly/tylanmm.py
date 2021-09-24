total = 0
for _ in range(int(input())):
    q, y = map(float, input().split())
    total += q * y
print(total)