n = int(input())
bats = list(map(int, input().split()))
real = []
for b in bats:
    if b > -1:
        real.append(b)
print(sum(real)/len(real))