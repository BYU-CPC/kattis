swords = [input() for _ in range(int(input()))]
tblr = [0, 0, 0, 0]
for s in swords:
    for i in range(4):
        tblr[i] += not int(s[i])
numSwords = min((tblr[0] + tblr[1]) // 2, (tblr[2] + tblr[3]) // 2)
print(numSwords, tblr[0] + tblr[1] - numSwords*2, tblr[2] + tblr[3] - numSwords*2)