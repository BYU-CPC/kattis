line = input()
score, numProbs, attempts = 0, 0, {}
while line != '-1':
    m, prob, isRight = line.split()
    m, isRight = int(m), isRight == 'right'
    if isRight:
        if prob in attempts:
            score += 20 * attempts.pop(prob)
        score += m
        numProbs += 1
    else:
        if prob in attempts:
            attempts[prob] += 1
        else:
            attempts[prob] = 1
    line = input()
print(numProbs, score)