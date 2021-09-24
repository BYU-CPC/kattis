n, m = map(int, input().split())
lists = [input().split() for _ in range(n)]
common = set(lists[0])
for l in lists[1:]:
    common &= set(l)
print(len(common))
for item in sorted(common):
    print(item)