n, m = map(int, input().split())
term = []
for num in range(1, m+1):
    if num % 3 == 0 and num % 5 == 0:
        term.append('fizzbuzz')
    elif num % 3 == 0:
        term.append('fizz')
    elif num % 5 == 0:
        term.append('buzz')
    else:
        term.append(str(num))

best = 0
best_candidate = 0
for candidate in range(n):
    ans = input().split()
    total = sum([ans[i] == term[i] for i in range(m)])
    if total > best:
        best = total
        best_candidate = candidate
print(best_candidate + 1)