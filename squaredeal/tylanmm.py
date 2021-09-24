rects = [tuple(map(int, input().split())) for _ in range(3)]
tests = [rects.copy()]          # 0 0 0
rects[0] = rects[0][::-1]
tests.append(rects.copy())      # 1 0 0
rects[1] = rects[1][::-1]
tests.append(rects.copy())      # 1 1 0
rects[2] = rects[2][::-1]
tests.append(rects.copy())      # 1 1 1
rects[1] = rects[1][::-1]
tests.append(rects.copy())      # 1 0 1
rects[0] = rects[0][::-1]
tests.append(rects.copy())      # 0 0 1
rects[1] = rects[1][::-1]
tests.append(rects.copy())      # 0 1 1
rects[2] = rects[2][::-1]
tests.append(rects.copy())      # 0 1 0

canMake = False
for r in tests:
    # test stacked orientation
    if r[0][1] == r[1][1] == r[2][1] and r[0][0] + r[1][0] + r[2][0] == r[0][1]:
        canMake = True
    # test horizontal orientation
    if r[0][0] == r[1][0] == r[2][0] and r[0][0] == r[0][1] + r[1][1] + r[2][1]:
        canMake = True

    # test c next to a b stack
    if r[0][1] == r[1][1] and r[2][0] == r[0][0] + r[1][0] and r[0][1] + r[2][1] == r[2][0]:
        canMake = True
    # test b next to a c stack
    if r[0][1] == r[2][1] and r[1][0] == r[0][0] + r[2][0] and r[0][1] + r[1][1] == r[1][0]:
        canMake = True
    # test a next to b c stack
    if r[1][1] == r[2][1] and r[0][0] == r[1][0] + r[2][0] and r[0][1] + r[1][1] == r[0][0]:
        canMake = True

    # test c on a b pair
    if r[0][0] == r[1][0] and r[2][1] == r[0][1] + r[1][1] and r[0][0] + r[2][0] == r[2][1]:
        canMake = True
    # test b on a c pair
    if r[0][0] == r[2][0] and r[1][1] == r[0][1] + r[2][1] and r[0][0] + r[1][0] == r[1][1]:
        canMake = True
    # test a on b c pair
    if r[1][0] == r[2][0] and r[0][1] == r[1][1] + r[2][1] and r[0][0] + r[1][0] == r[0][1]:
        canMake = True

print('YES' if canMake else 'NO')