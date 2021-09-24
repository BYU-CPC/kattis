x = int(input())
n = int(input())
total = x
for i in range(n):
    total -= int(input())
    total += x
print(total)