center, *letters = input()
letters = set(letters) | {center}
for _ in range(int(input())):
    w = input()
    word = set(w)
    if len(w) > 3 and center in word and len(word.intersection(letters)) == len(word):
        print(w)