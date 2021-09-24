k = int(input())
answer = 1
prev = int(input())
for _ in range(k-1):
    curr = int(input())
    if curr < prev:
        answer += 1
    prev = curr
print(answer)