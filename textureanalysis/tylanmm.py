line = input()
lineNum = 1
while line != 'END':
    line = line.split('*')[1:-1]
    for i in range(1, len(line)):
        if len(line[i]) != len(line[i-1]):
            print(f'{lineNum} NOT EVEN')
            break
    else:
        print(f'{lineNum} EVEN')
    
    line = input()
    lineNum += 1