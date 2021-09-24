n, m, o = map(int, input().split())
plots = sorted(map(int, input().split()))
circ = sorted(map(int, input().split()))
square = sorted(map(int, input().split()))

i, j, k = 0, 0, 0
filled = 0
while i < n:
    if j < m and circ[j] < plots[i]:
        filled += 1
        j += 1
    elif k < o and (2 * square[k]**2)**0.5 < plots[i]*2:
        filled += 1
        k += 1
    i += 1

print(filled)