for t in range(int(input())):
    n = int(input())
    total = 0
    hi = 0
    hiNum = 0
    for i in range(1, n+1):
        num = int(input())
        total += num
        if num > hiNum:
            hi = i
            hiNum = num
        elif num == hiNum:
            hi = 0
    
    if hi == 0:
        print('no winner')
    else:
        print('majority' if hiNum * 2 > total else 'minority', 'winner', hi)