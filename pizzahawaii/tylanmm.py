t = int(input())
for i in range(t):
    n = int(input())
    ingItal = {}
    ingEngl = {}
    for i in range(n):
        name = input()
        italian = set(input().split()[1:])
        english = set(input().split()[1:])
        for ing in italian:
            if ing not in ingItal:
                ingItal[ing] = set()
            ingItal[ing].add(name)
        for ing in english:
            if ing not in ingEngl:
                ingEngl[ing] = set()
            ingEngl[ing].add(name)
    sortedItal = sorted(ingItal)
    sortedEngl = sorted(ingEngl)
    for ing1 in sortedItal:
        for ing2 in sortedEngl:
            if ingItal[ing1] == ingEngl[ing2]:
                print("(" + ing1 + ", " + ing2 + ")")
    print()