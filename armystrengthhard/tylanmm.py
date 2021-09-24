for _ in range(int(input())):
    input()
    ng, nm = map(int, input().split())
    gArmy = list(map(int, input().split()))
    mgArmy = list(map(int, input().split()))
    
    gHi = max(gArmy)
    mgHi = max(mgArmy)
    
    if gHi >= mgHi:
        print('Godzilla')
    else:
        print('MechaGodzilla')