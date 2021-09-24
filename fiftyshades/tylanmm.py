n = int(input())
words = [input().lower() for _ in range(n)]
answer = 0
for w in words:
    if 'pink' in w or 'rose' in w:
        answer += 1
print(answer if answer else 'I must watch Star Wars with my daughter')