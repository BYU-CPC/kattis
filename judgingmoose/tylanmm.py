l, r = map(int, input().split())
if l == 0 and r == 0:
    print('Not a moose')
elif l == r:
    print('Even %d' % (2*l))
else:
    print('Odd %d' % (2*max(l, r)))