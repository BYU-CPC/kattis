from collections import deque
from sys import stdin, stdout

n = int(stdin.readline())
while n:
    pile = [0, deque(), deque()]
    p1Size = 0

    for _ in range(n):
        line = stdin.readline().split()
        com, amt = line[0], int(line[1])

        if com == 'DROP':
            stdout.write('DROP 1 %d\n' % amt)
            pile[1].append(amt)
            p1Size += amt
        else:
            taken = 0
            sinceSwitch = 0
            while taken < amt:
                if pile[2]:
                    take = pile[2].popleft()
                    sinceSwitch += take
                    taken += take
                    if taken > amt:
                        pile[2].appendleft(taken - amt)
                else:
                    if sinceSwitch:
                        stdout.write('TAKE 2 %d\n' % sinceSwitch)
                    pile[2] = pile[1]
                    pile[1] = deque()
                    stdout.write('MOVE 1->2 %d\n' % p1Size)
                    p1Size = 0
                    sinceSwitch = 0
            
            stdout.write('TAKE 2 %d\n' % (sinceSwitch - (taken - amt)))

    stdout.write('\n')
    n = int(stdin.readline())

stdout.flush()