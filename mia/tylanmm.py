roll = input()
while roll != '0 0 0 0':
    s0, s1, r0, r1 = map(int, roll.split())
    p1 = f'{max(s0, s1)}{min(s0, s1)}'
    p2 = f'{max(r0, r1)}{min(r0, r1)}'
    if p1 == '21':
        if p2 == '21':
            print('Tie.')
        else:
            print('Player 1 wins.')
    elif p1[0] == p1[1]:
        if p2 == '21':
            print('Player 2 wins.')
        elif p2[0] == p2[1]:
            if p1 == p2:
                print('Tie.')
            else:
                print(f'Player {1 if p1 > p2 else 2} wins.')
        else:
            print('Player 1 wins.')
    else:
        if p2 == '21':
            print('Player 2 wins.')
        elif p2[0] == p2[1]:
            print('Player 2 wins.')
        else:
            if p1 == p2:
                print('Tie.')
            else:
                print(f'Player {1 if p1 > p2 else 2} wins.')
    
    roll = input()