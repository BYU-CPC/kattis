from itertools import combinations
expr = input()
pairs = []
stack = []
for i in range(len(expr)):
    if expr[i] == '(':
        stack.append(i)
    elif expr[i] == ')':
        pairs.append((stack.pop(), i))

combos = []
for i in range(1, len(pairs)+1):
    combos += list(combinations(pairs, i))

results = set()
for c in combos:
    toSkip = set()
    for a, b in c:
        toSkip.add(a)
        toSkip.add(b)
    results.add(''.join([expr[i] for i in range(len(expr)) if i not in toSkip]))
print('\n'.join(sorted(list(results))))