def solve(samples:list) -> int:

    edges = []
    min_unlikeliness = -1

    # YOUR CODE HERE

    return edges, min_unlikeliness

if __name__ == '__main__':

    n, k = map(int,input().split(' '))

    samples = []
    for _ in range(n):
        samples.append( input() )

    edges, min_u = solve(samples)

    print(min_u)
    for u,v in edges:
        print(u,v)
