raw = list(map(int, input().split()))
shape1 = [(raw[i], raw[i+1]) for i in range(1, 2*raw[0]+1, 2)]
raw = list(map(int, input().split()))
shape2 = [(raw[i], raw[i+1]) for i in range(1, 2*raw[0]+1, 2)]

def read(shape):
    xs = [0]*3001
    ys = [0]*3001
    for x, y in shape:
        xs[x] = 1
        ys[y] = 1
    for i in range(1, 3001):
        xs[i] += xs[i-1]
        ys[i] += ys[i-1]

    for i in range(len(shape)):
        shape[i] = (xs[shape[i][0]] - 1, ys[shape[i][1]] - 1)

def rotate90(shape):
    n = len(shape)//2
    for i in range(len(shape)):
        shape[i] = (n-shape[i][1]-1, shape[i][0])

read(shape1)
read(shape2)
if len(shape1) != len(shape2):
    print('no')
else:
    for _ in range(4):
        rotate90(shape2)
        if shape1[0] not in shape2:
            continue
        
        i = shape2.index(shape1[0])
        if i:
            shape2 = shape2[i:] + shape2[:i]
        if shape1 == shape2:
            print('yes')
            break
    else:
        print('no')