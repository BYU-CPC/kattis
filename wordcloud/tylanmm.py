from math import ceil

t = 1
w, n = map(int, input().split())
while w and n:
    words = []
    cmax = 0
    for _ in range(n):
        word, cw = input().split()
        cw = int(cw)
        cmax = max(cmax, cw)
        words.append((word, cw))
    
    height, lineWidth, lineHeight = 0, 0, 0
    for word, cw in words:
        p = 8 + ceil(40*(cw - 4) / (cmax - 4))
        width = ceil(9/16 * len(word) * p)
        if lineWidth == 0:
            lineHeight = p
            lineWidth = width
        elif lineWidth + 10 + width <= w:
            lineHeight = max(lineHeight, p)
            lineWidth += 10 + width
        else:
            height += lineHeight
            lineHeight = p
            lineWidth = width
    height += lineHeight
    print(f'CLOUD {t}: {height}')

    w, n = map(int, input().split())
    t += 1