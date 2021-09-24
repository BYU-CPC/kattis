word = set(input())
perm = input()

bad = 0
good = 0
for c in perm:
    if c in word:
        good += 1
    else:
        bad += 1
    
    if bad == 10:
        print('LOSE')
        break
    elif good == len(word):
        print('WIN')
        break
