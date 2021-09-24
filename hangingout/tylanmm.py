l, x = map(int, input().split())
total = 0
rej = 0
for _ in range(x):
    dir, amt = input().split()
    amt = int(amt)
    if dir == "leave":
        total -= amt
    else:
        if total + amt <= l:
            total += amt
        else:
            rej += 1
print(rej)