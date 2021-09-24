n = int(input())
while n:
    num = ['?'] * 32
    for _ in range(n):
        instr = input().split()
        
        if instr[0] == 'CLEAR':
            i = int(instr[1])
            num[i] = 0
        
        elif instr[0] == 'SET':
            i = int(instr[1])
            num[i] = 1
        
        elif instr[0] == 'OR':
            i, j = int(instr[1]), int(instr[2])
            if num[i] == 1 or num[j] == 1:
                num[i] = 1
            elif num[i] == 0 and num[j] == 0:
                num[i] = 0
            else:
                num[i] = '?'
        
        else:
            i, j = int(instr[1]), int(instr[2])
            if num[i] == 1 and num[j] == 1:
                num[i] = 1
            elif num[i] == 0 or num[j] == 0:
                num[i] = 0
            else:
                num[i] = '?'
        
    print(''.join(map(str, num[::-1])))
    n = int(input())