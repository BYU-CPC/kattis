n, bev = int(input()), input()
while n > 1:
    print(f'{n} bottles of {bev} on the wall, {n} bottles of {bev}.')
    n -= 1
    print(f'Take one down, pass it around, {n} %s of {bev} on the wall.\n' % ('bottles' if n > 1 else 'bottle'))

print(f'{n} bottle of {bev} on the wall, {n} bottle of {bev}.')
print(f'Take it down, pass it around, no more bottles of {bev}.')