from string import ascii_lowercase, ascii_uppercase
s = input()
count = [0]*4
for c in s:
    if c == '_': count[0] += 1
    elif c in ascii_lowercase: count[1] += 1
    elif c in ascii_uppercase: count[2] += 1
    else: count[3] += 1

for i in range(4):
    print(count[i] / len(s))