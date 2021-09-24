hi, hiS = 0, 0
for i in range(1, 6):
    score = sum(map(int, input().split()))
    if score > hiS:
        hi = i
        hiS = score
print(hi, hiS)