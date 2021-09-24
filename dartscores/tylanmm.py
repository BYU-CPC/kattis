for _ in range(int(input())):
    n = int(input())
    score = 0
    for _ in range(n):
        x, y = map(int, input().split())
        dist = (x**2 + y**2)**0.5
        if dist > 200:
            continue
        p = dist // 20 + (1 if dist % 20 or dist == 0 else 0)
        score += 11 - p
    print(int(score))