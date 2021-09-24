l, w = map(int, input().split())
canMake = [['']*(l+1) for _ in range(w+1)]
canMake[0][0] = ' '
for weight in range(w):
    for length in range(l):
        for letter in range(26):
            if weight + letter + 1 <= w:
                if canMake[weight + letter + 1][length + 1]: continue
                elif canMake[weight][length]: canMake[weight + letter + 1][length + 1] = canMake[weight][length] + chr(letter + 97)
            else: break
print(canMake[w][l][1:] if canMake[w][l] else 'impossible')