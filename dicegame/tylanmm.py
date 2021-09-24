def E(dice):
    return (dice[0] + dice[1])/2 + (dice[2] + dice[3])/2

g = E(list(map(int, input().split())))
e = E(list(map(int, input().split())))
if g > e:
    print("Gunnar")
elif g < e:
    print("Emma")
else:
    print("Tie")