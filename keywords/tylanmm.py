n = int(input())
words = set()
for _ in range(n):
    words.add(input().lower().replace('-', ' '))
    
print(len(words))