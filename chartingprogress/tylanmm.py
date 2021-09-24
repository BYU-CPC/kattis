from sys import stdin

logs = [log.split() for log in stdin.read().split('\n\n')]
for log in logs:
    seen = 0
    cols = len(log[0])
    for i in range(len(log)):
        freq = log[i].count('*')
        print('.'*(cols - freq - seen) + '*'*freq + '.'*seen)
        seen += freq
    print()    