n = int(input())
socks = list(map(int, input().split()))
aux = []

moves = 0
while socks:
    if aux and socks[-1] == aux[-1]:
        socks.pop()
        aux.pop()
    else:
        aux.append(socks.pop())
    moves += 1

print('impossible' if aux else moves)