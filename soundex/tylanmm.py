from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(200000)

def _i():
    return stdin.readline()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

code = {letter: '' for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
code['B'] = code['F'] = code['P'] = code['V'] = '1'
code['C'] = code['G'] = code['J'] = code['K'] = code['Q'] = code['S'] = code['X'] = code['Z'] = '2'
code['D'] = code['T'] = '3'
code['L'] = '4'
code['M'] = code['N'] = '5'
code['R'] = '6'

def solve(word):
    res = []
    for i in range(len(word)):
        c = code[word[i]]
        if len(res) == 0 or res[-1] != c:
            res.append(c)
    return ''.join(res)

for line in stdin:
    _p(solve(list(line.strip())))

stdout.flush()