'''
n, b, h, and w are as described in the problem
price[i] = price for one person staying the weekend at hotel i
beds[i][w] = number of available beds at hotel i on weekend w
return nothing: print the minimum cost, or 'stay home'
'''
def solve(n: int, b: int, h: int, w: int, price: list[int], beds: list[list[int]]) -> None:
    pass

if __name__ == '__main__':
    n, b, h, w = map(int, input().split())
    price = []
    beds = []
    for _ in range(h):
        price.append(int(input()))
        beds.append(list(map(int, input().split())))
    solve(n, b, h, w, price, beds)