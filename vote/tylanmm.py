for _ in range(int(input())):
    n = int(input())
    total, hi, hiC = 0, 0, 0
    for i in range(n):
        votes = int(input())
        total += votes
        if votes > hi:
            hi = votes
            hiC = i+1
        elif votes == hi:
            hiC = 0
    
    if hiC:
        if hi >= (total)//2 + 1:
            print(f'majority winner {hiC}')
        else:
            print(f'minority winner {hiC}')
    else:
        print('no winner')