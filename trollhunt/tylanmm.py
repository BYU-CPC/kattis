b, k, g = map(int, input().split())
count, groups = 0, k//g
while b > 1:
    b -= groups
    count += 1
print(count)