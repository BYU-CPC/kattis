game = input()
score = {'A':0, 'B':0}
for i in range(0, len(game), 2):
    score[game[i]] += int(game[i+1])

print('A' if score['A'] > score['B'] else 'B')