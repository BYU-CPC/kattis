w, p = map(int, input().split())
parts = [0] + list(map(int, input().split())) + [w]
sizes = set()
for i in range(p+1):
    for j in range(i+1, p+2):
        sizes.add(parts[j] - parts[i])
print(' '.join(map(str, sorted(list(sizes)))))