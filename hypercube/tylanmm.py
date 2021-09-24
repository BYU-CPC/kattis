n, a, b = input().split()
n = int(n)

def find(num):
    lo, hi, prev = 0, 2**n - 1, 0
    for bit in num:
        if bit == '0':
            if prev:
                lo = (lo + hi) // 2 + 1
            else:
                hi = (lo + hi) // 2
        else:
            if prev:
                hi = (lo + hi) // 2
            else:
                lo = (lo + hi) // 2 + 1
            prev ^= 1

    return lo

print(abs(find(a) - find(b)) - 1)
    
# 0 1 3 2 6 7 5 4
# 0 1
# 00 01 11 10
# 000 001 011 010 110 111 101 100
# 0000 0001 0011 0010 0110 0111 0101 0100 1100 1101 1111 1110 1010 1011 1001 1000