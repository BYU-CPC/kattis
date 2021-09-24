from sys import stdin

for line in stdin:
    print('yes' if 'problem' in line.lower() else 'no')