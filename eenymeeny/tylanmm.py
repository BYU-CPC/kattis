w = len(input().split()) - 1
n = int(input())
kids = [input() for _ in range(n)]

teams = [[], []]
last = team = 0
while kids:
    last = (last + w) % len(kids)
    teams[team].append(kids.pop(last))
    team ^= 1

print(len(teams[0]))
print('\n'.join(teams[0]))
print(len(teams[1]))
print('\n'.join(teams[1]))