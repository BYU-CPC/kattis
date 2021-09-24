def count(s, search):
    if len(s) < len(search): return 0

    total, n = 0, len(s)
    for i in range(len(s)-len(search)+1):
        if s[i] != search[0]: continue
        for j in range(1, len(search)):
            if i+j == n or search[j] != s[i+j]:
                break
        else:
            total += 1
    return total

line = input()
while line != '0':
    s, l = line.split()
    a = count(l, s)
    
    delete = set()
    for i in range(len(s)):
        delete.add(s[:i] + s[i+1:])
    b = sum([count(l, word) for word in delete])
    
    insert = set()
    for i in range(len(s)+1):
        for x in 'AGCT':
            insert.add(s[:i] + x + s[i:])
    c = sum([count(l, word) for word in insert])
    
    print(a, b, c)
    line = input()