from itertools import permutations

probs = [0, 1, 0.5, 0.666666, 0.625, 0.633333, 0.631944, 0.632142, 0.632118, 0.63212]
n = int(input())
if n <= 9:
    print(probs[n])
else:
    print(probs[9])