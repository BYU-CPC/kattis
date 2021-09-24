def findAlign(word1, word2):
    for i in range(len(word1)):
        if word1[i] != word2[0]: continue
        for j in range(len(word2)-i):
            if word2[j] != word1[i+j]:
                break
        else:
            return i
    return len(word1)

for _ in range(int(input())):
    k, w = map(int, input().split())
    word = input()
    total = k
    for _ in range(w-1):
        nextWord = input()
        total += findAlign(word, nextWord)
        word = nextWord
    print(total)