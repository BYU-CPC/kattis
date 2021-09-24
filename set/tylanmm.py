cards = input().split() + input().split() + input().split() + input().split()
none = True
for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            for l in range(4):
                if len({cards[i][l], cards[j][l], cards[k][l]}) == 2:
                    break
            else:
                none = False
                print(i+1, j+1, k+1)
if none:
    print('no sets')