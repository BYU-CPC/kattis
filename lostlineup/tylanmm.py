n, people = int(input()), list(map(int, input().split()))
res = [0]*n
res[0] = 1
for i in range(n-1):
    res[people[i]+1] = i+2
print(' '.join(map(str, res)))