n, items = int(input()), sorted(list(map(int, input().split())), reverse=True)
discount, i = 0, 0
while i < n:
    if i + 3 <= n:
        discount += items[i+2]
        i += 3
    else:
        break
print(discount)