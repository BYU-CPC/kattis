num = 0
for _ in range(int(input())):
    num <<= 1
    num += input() == 'O'
print(num)