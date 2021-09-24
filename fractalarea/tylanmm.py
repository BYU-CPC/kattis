import math
def compute(r, n):
    area = r**2
    for i in range(0, n - 1):
        r /= 2
        area += (4 * 3**i) * r**2
    return area * math.pi

for i in range(int(input())):
    r, n = tuple(map(int, input().split()))
    print(compute(r, n))