line = input()
while line != '0':
    n, s = line.split()
    n = int(n)
    s = s[::-1]
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
    vals = {symbols[i]:i for i in range(28)}
    
    res = ''
    for c in s:
        res += symbols[(vals[c] + n) % 28]
    print(res)

    line = input()