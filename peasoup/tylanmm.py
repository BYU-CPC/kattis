done = False
for _ in range(int(input())):
    k, name = int(input()), input()
    hasPea, hasPan = False, False
    for f in range(k):
        food = input()
        hasPea |= food == 'pea soup'
        hasPan |= food == 'pancakes'
    if hasPea and hasPan and not done:
        print(name)
        done = True
if not done:
    print('Anywhere is fine I guess')