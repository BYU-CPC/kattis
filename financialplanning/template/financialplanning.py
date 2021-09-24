def solve(options:list, min_to_retire: int) -> int:

    # YOUR CODE HERE

    return 0

if __name__ == '__main__':

    n, M = map(int,input().split(' '))

    options = []
    for _ in range(n):
        options.append( tuple(map(int,input().split(' '))) )
    print( solve(options, M) )
