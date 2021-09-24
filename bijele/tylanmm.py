correct = [1, 1, 2, 2, 2, 8]
have = list(map(int, input().split()))
need = [correct[i] - have[i] for i in range(6)]
print(' '.join(map(str, need)))