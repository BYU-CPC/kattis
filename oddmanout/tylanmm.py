for i in range(int(input())):
    g = int(input())
    seen = set()
    for c in input().split():
        if c not in seen:
            seen.add(c)
        else:
            seen.remove(c)
    print("Case #%d: %s" % (i+1, seen.pop()))