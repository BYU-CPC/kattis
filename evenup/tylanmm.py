n = int(input())
s = []
cards = map(int, input().split())

for c in cards:
    if s and (s[-1] + c) % 2 == 0:
        s.pop()
    else:
        s.append(c)

print(len(s))