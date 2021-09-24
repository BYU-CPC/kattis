input()
row, board = 8, []
for _ in range(8):
    line = input().split('|')[1:-1]
    for i in range(8):
        p = line[i][1]
        if p not in '.:':
            line[i] = p + chr(97 + i) + str(row)
    board.append(line)
    input()
    row -= 1

pieces = {'White':[], 'Black':[]}
for i in range(8):
    for j in range(8):
        if board[i][j][0] >= 'a':
            pieces['Black'].append(board[i][j][0].upper() + board[i][j][1:])
        if board[-i-1][j][0] < 'a' and board[-i-1][j][0] >= 'A':
            pieces['White'].append(board[-i-1][j])

prec = {'K': 1, 'Q': 2, 'R': 3, 'B': 4, 'N': 5, 'P': 6}
for color in pieces:
    pieces[color].sort(key=lambda x:prec[x[0]])
    for i in range(len(pieces[color])):
        if pieces[color][i][0] == 'P':
            pieces[color][i] = pieces[color][i][1:]
    print(f'{color}: ' + ','.join(pieces[color]))