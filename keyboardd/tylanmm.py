og = input()
stick = input()
j = 0
keys = set()
for i in range(len(og)):
    if og[i] != stick[j]:
        keys.add(stick[j])
    while j < len(stick) and og[i] != stick[j]:
        j += 1
    j += 1

if j < len(stick):
    keys.add(stick[-1])

print(''.join(keys))