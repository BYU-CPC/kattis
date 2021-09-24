def solve(rooms:list, num_to_close_off: int) -> int:

    # YOUR CODE HERE

    return 0

if __name__ == '__main__':

    N, k = map(int,input().split(' '))
    rooms = []
    for _ in range(N):
        rooms.append( list(map(int,input().split(' '))) )
    print( solve(rooms, k) )
