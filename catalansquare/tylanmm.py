n = int(input())
cat = [1, 1]
for i in range(2, n+1):
    cat.append(cat[i-1]*(2*i)*(2*i-1) // (i*(i+1)))

s = 0
for k in range(n+1):
    s += cat[k]*cat[n-k]

print(s)