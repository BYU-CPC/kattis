from sys import stdin

f = stdin.read().strip().split('\n')
i = 0
while i < len(f):
    _, *do = f[i].split()
    _, *co = f[i+1].split()
    do = set(do)
    co = set(co)

    n = int(f[i+2])
    rels = [f[j].split(' -> ') for j in range(i+3, i+3+n)]
    i += 3 + n
    
    inj = True
    notFunc = False
    for x, y in rels:
        if x not in do:
            notFunc = True
            break
        do.discard(x)
        if y not in co:
            inj = False
        co.discard(y)
    sur = not co

    if notFunc:
        print('not a function')
    elif inj and sur:
        print('bijective')
    elif inj:
        print('injective')
    elif sur:
        print('surjective')
    else:
        print('neither injective nor surjective')