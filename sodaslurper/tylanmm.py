e, f, c = map(int, input().split())
count = 0
bottles = e + f
while bottles >= c:
    count += bottles // c
    bottles = bottles // c + bottles % c
print(count)