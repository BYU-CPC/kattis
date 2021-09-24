n = int(input())
for _ in range(n):
    line = input()
    i = line.find('Simon says')
    if i == 0:
        print(line[10:])