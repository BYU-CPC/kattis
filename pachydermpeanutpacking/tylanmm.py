while True:
    n = int(input())
    if n == 0:
        break
    boxes = []
    for i in range(n):
        line = input().split()
        size = line[-1]
        box = list(map(float, line[:-1]))
        box.append(size)
        boxes.append(tuple(box))
    
    m = int(input())
    for i in range(m):
        line = input().split()
        x, y = tuple(map(float, line[:-1]))
        size = line[-1]
        inBox = False
        for b in boxes:
            if (b[0] <= x and x <= b[2]) and (b[1] <= y and y <= b[3]):
                inBox = True
                if b[4] == size:
                    print(size, 'correct')
                else:
                    print(size, b[4])
                break
        if not inBox:
            print(size, 'floor')