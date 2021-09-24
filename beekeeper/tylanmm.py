def countPairs(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count, i = 0, 0
    while i < (len(word) - 1):
        if word[i] in vowels and word[i] == word[i+1]:
            count += 1
            i += 1
        i += 1
    return count

n = int(input())
while n != 0:
    hiW = input()
    hi = countPairs(hiW)
    for _ in range(n-1):
        word = input()
        count = countPairs(word)
        if count > hi:
            hiW = word
            hi = count
    print(hiW)
    n = int(input())