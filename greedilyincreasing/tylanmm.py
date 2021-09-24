n = int(input())
res = []
lo = 0
for num in map(int, input().split()):
    if num > lo:
        res.append(num)
        lo = num
print(len(res))
print(*res)