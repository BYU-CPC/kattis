c = float(input())
l = int(input())
total = 0
for i in range(l):
    lawn = tuple(map(float, input().split()))
    total += c * lawn[0] * lawn[1]
print('{:.7f}'.format(total))