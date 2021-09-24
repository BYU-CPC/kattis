def polyMult(poly1, poly2):
    polyOut = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            polyOut[i + j] += poly1[i] * poly2[j]
    return polyOut

for t in range(int(input())):
    input()
    poly1 = list(map(int, input().split()))
    input()
    poly2 = list(map(int, input().split()))

    result = polyMult(poly1, poly2)
    print(len(result) - 1)
    print(" ".join(map(str, result)))