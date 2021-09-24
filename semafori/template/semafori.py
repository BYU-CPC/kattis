def solve(lights:list, road_length: int) -> int:

    # YOUR CODE HERE

    return 0

if __name__ == '__main__':

    N, L = map(int,input().split(' '))

    lights = []
    for _ in range(N):
        lights.append( tuple(map(int,input().split(' '))) )
        
    print( solve(lights, L) )
