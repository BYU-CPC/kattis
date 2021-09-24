total = 0
for i in range(int(input())):
    line = input()
    num = int(line[:-1])
    exp = int(line[-1])
    total += num ** exp
print(total)