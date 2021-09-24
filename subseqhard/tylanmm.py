from sys import stdin, stdout

def _i():
    return stdin.readline().strip()

def _p(x, end='\n'):
    stdout.write(str(x) + end)

for _ in range(int(_i())):
    _i()

    n = int(_i())
    seen = {0: 1}
    total = 0
    count = 0
    for num in map(int, _i().split()):
        total += num
        if total - 47 in seen:
            count += seen[total-47]
        
        if total in seen:
            seen[total] += 1
        else:
            seen[total] = 1
    
    _p(count)

stdout.flush()

# prefix sum, two sum