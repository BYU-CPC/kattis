n, k = map(int, input().split())
total = sum([int(input()) for _ in range(k)])
print(f'{(total - 3*(n-k)) / n} {(total + 3*(n-k)) / n}')