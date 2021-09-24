from sys import stdin

def solve(line):
    s = []
    for sym in line[::-1]:
        try:
            sym = int(sym)
            s.append(str(sym))
        except ValueError:
            if sym in '+-*' and (s[-1].isnumeric() or s[-1][1:].isnumeric()) and (s[-2].isnumeric() or s[-2][1:].isnumeric()):
                s.append(str(eval(s.pop() + sym + s.pop())))
            else:
                s.append(sym)
    return s[::-1]

i = 1
for line in stdin.readlines():
    print(f'Case {i}: {" ".join(solve(line.split()))}')
    i += 1