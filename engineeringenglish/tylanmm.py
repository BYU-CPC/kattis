from sys import stdin

seen = set()
for line in stdin:
    line = line.split()
    for i in range(len(line)):
        if line[i].lower() in seen:
            line[i] = '.'
        seen.add(line[i].lower())
    print(' '.join(line))