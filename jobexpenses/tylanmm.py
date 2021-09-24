n = int(input())
total = 0
for num in map(int, input().split()):
    total -= num if num < 0 else 0
print(total)