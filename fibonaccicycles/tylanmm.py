q = int(input())
for _ in range(q):
    k = int(input())
    seen = [0]*k
    prev1, prev2, = 1, 1
    for i in range(2, k+3):
        val = (prev1 + prev2) % k
        prev1, prev2 = prev2, val
        if seen[val]: 
            print(seen[val])
            break
        seen[val] = i