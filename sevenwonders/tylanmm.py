cards = input()
points = {'T':0, 'C':0, 'G':0}
for c in cards:
    points[c] += 1
total = 0
low = len(cards)
for p in points:
    low = min(low, points[p])
    total += points[p]**2

print(total + 7*low)