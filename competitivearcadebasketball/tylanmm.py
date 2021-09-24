n, p, m = map(int, input().split())
score = {input(): 0 for _ in range(n)}
winner = False
for _ in range(m):
    name, points = input().split()
    points = int(points)
    if score[name] < p and score[name] + points >= p:
        print(name, 'wins!')
        winner = True
    score[name] += points
if not winner:
    print('No winner!')