def gcd(a, b):
    return gcd(b, a % b) if b else a

def lcm(a, b):
    return a * (b // gcd(a, b))

p, q, s = map(int, input().split())
print('yes' if lcm(p, q) <= s else 'no')