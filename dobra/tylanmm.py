chars = list(input())
scores = [i for i in range(len(chars)) if chars[i] == '_']
vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

def canPlace(i, letters):
    # check --i, -i-, and i--
    if i > 1 and (chars[i-2] in letters) and (chars[i-1] in letters):
        return False
    if i > 0 and i < len(chars)-1 and (chars[i-1] in letters) and (chars[i+1] in letters):
        return False
    if i < len(chars)-2 and (chars[i+1] in letters) and (chars[i+2] in letters):
        return False
    return True

def solve(underI):
    if underI == len(scores):
        return 1 if 'L' in chars else 0
    
    count = 0
    if canPlace(scores[underI], vowels):
        chars[scores[underI]] = 'A'
        count += 5*solve(underI + 1)
    
    if canPlace(scores[underI], consonants):
        chars[scores[underI]] = 'L'
        count += solve(underI + 1)

        chars[scores[underI]] = 'B'
        count += 20*solve(underI + 1)
    
    chars[scores[underI]] = '_'
    return count

print(solve(0))