num = input()
while num != 'END':
    i = 0
    while num != '1':
        num = str(len(str(num)))
        i += 1
    print(i + 1)
    num = input()