for t in range(1, int(input())+1):
    r, p, d = map(int, input().split())
    factor = d / p
    ingredients = []
    main = 0
    for i in range(r):
        ing, w, pct = input().split()
        w = float(w)
        pct = float(pct) / 100
        ingredients.append([ing, w, pct])
        main = i if pct == 1 else main
    
    ingredients[main][1] *= factor
    for i in range(r):
        if i == main: continue
        ingredients[i][1] = round(ingredients[i][2] * ingredients[main][1], 1)
    
    print(f'Recipe # {t}')
    for ing, w, pct in ingredients:
        print(f'{ing} {w}')
    print('-'*40)