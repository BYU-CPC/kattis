order = {'upper': 0, 'middle': 1, 'lower': 2}

for _ in range(int(input())):
    n = int(input())
    people = {}
    hi = 0
    for i in range(n):
        name, c = input().split(': ')
        c = c[:-6].split('-')[::-1]
        for j in range(len(c)):
            c[j] = order[c[j]]
        people[name] = c
        hi = max(hi, len(c))
    
    for p in people:
        people[p].extend([1] * (hi - len(people[p])))
        people[p] = tuple(people[p])
    
    ordered = sorted(people)
    ordered = sorted(ordered, key=lambda p: people[p])
    for p in ordered:
        print(p)
    print('='*30)