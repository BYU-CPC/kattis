for i in range(int(input())):
    line = input().split()
    b = int(line[0])
    p = float(line[1])

    abpmMin = 60 / (p / (b-1))
    bpm = 60 * b / p
    abpmMax = 60 / (p / (b+1))

    print('{:.4f} {:.4f} {:.4f}'.format(abpmMin, bpm, abpmMax))