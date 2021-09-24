n, w, h = map(int, input().split())
d = w*w + h*h
for _ in range(n):
    l = int(input())
    if l*l <= d:
        print('DA')
    else:
        print('NE')