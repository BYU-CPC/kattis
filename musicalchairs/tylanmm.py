n = int(input())
prof = list(map(int, input().split()))
for i in range(n):
    prof[i] = (prof[i], i+1)

i = 0
while len(prof) > 1:
    i = (i + prof[i][0] - 1) % len(prof)
    prof.pop(i)
    if i >= len(prof):
        i = 0
print(prof[0][1])