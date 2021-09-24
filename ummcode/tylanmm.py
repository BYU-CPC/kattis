raw = input().split()
msg = []
for word in raw:
    w = []
    for c in word:
        if c in 'um':
            w.append('1' if c == 'u' else '0')
        elif c.isalnum():
            break
    else:
        msg.extend(w)

final = []
for i in range(0, len(msg), 7):
    final.append(chr(int(''.join(msg[i:i+7]), 2)))
print(''.join(final))