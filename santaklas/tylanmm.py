import math
H, v = map(int, input().split())
if v <= 180:
    print('safe')
elif v < 270:
    print(int(H/math.sin(math.radians(v-180))))
elif v > 270:
    print(int(H/math.sin(math.radians(360-v))))
else:
    print(H)