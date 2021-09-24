n = int(input())
countries = [tuple(map(int, input().split())) for _ in range(n)]

totalP = totalU = 0
for a, b in countries:
    totalP += a
    totalU += b

total = 0
for a, b in countries:
    total += a * (totalP - a) * (totalU - b)
    total -= 2 * (a * b) * (totalP - a)
print(total)