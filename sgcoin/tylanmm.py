mod = int(1e9) + 7

def get_token(prev, trans):
    v = prev
    for c in trans:
        v = (v*31 + ord(c)) % mod
    return (990000000 - ((v*7) % mod)) % mod

h = int(input())
tokenA = get_token(h, 'a')
tokenB = get_token(990000000, 'b')
print('a', tokenA)
print('b', tokenB)