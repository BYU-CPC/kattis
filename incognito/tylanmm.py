for _ in range(int(input())):
    n = int(input())
    cats = {}
    for _ in range(n):
        name, cat = input().split()
        if cat not in cats:
            cats[cat] = 1
        cats[cat] += 1
    
    total = 1
    for cat in cats:
        total *= cats[cat]
    print(total - 1)