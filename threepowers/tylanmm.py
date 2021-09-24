n = int(input())
while n:
    seq = []
    n -= 1
    n = f'{n:b}'[::-1]
    for i in range(len(n)):
        if n[i] == '1':
            seq.append(str(3 ** i))
    if seq:
        print('{ %s }' % ', '.join(seq))
    else:
        print('{ }')
    n = int(input())