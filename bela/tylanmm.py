table = {'A':[11, 11], 'K':[4, 4], 'Q':[3, 3], 'J':[20, 2], 'T':[10, 10], '9':[14, 0], '8':[0, 0], '7':[0, 0]}
n, b = input().split()
n = int(n)
score = 0
for _ in range(4*n):
    val, suit = input()
    score += table[val][suit != b]
print(score)