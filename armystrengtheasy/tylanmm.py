for _ in range(int(input())):
    input()
    ng, nm = map(int, input().split())
    gArmy = sorted(list(map(int, input().split())), reverse=True)
    mgArmy = sorted(list(map(int, input().split())), reverse=True)
    while gArmy and mgArmy:
        if gArmy[-1] < mgArmy[-1]:
            gArmy.pop()
        else:
            mgArmy.pop()
    print('Godzilla' if gArmy else 'MechaGodzilla')