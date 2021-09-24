for _ in range(int(input())):
    prob = input()
    if '+' in prob:
        a, b = map(int, prob.split('+'))
        print(a + b)
    else:
        print('skipped')