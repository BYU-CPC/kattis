n = int(input())
answer = input()
a, aScore = 'ABC' * 34, 0
b, bScore = 'BABC' * 25, 0
g, gScore = 'CCAABB' * 17, 0
for i in range(n):
    aScore += a[i] == answer[i]
    bScore += b[i] == answer[i]
    gScore += g[i] == answer[i]
m = max(aScore, bScore, gScore)
print(m)
if aScore == m:
    print('Adrian')
if bScore == m:
    print('Bruno')
if gScore == m:
    print('Goran')