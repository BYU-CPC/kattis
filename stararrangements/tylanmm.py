S = int(input())
print('%d:' % S)
for i in range(2, (S+1)//2 + 1):
    if S % (2*i - 1) == 0:              # even num rows, alternating sizes
        print('%d,%d' % (i, i-1))
    elif (S - i) % (2*i - 1) == 0:      # odd num rows, alternating sizes
        print('%d,%d' % (i, i-1))
    if S % i == 0:                      # any num rows, same size
        print('%d,%d' % (i, i))