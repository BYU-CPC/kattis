prev = 2
for i in range(int(input())):
    prev += prev - 1

count = 0
for i in range(1, prev + 1):
    count += i * 2 - 1
print(count)