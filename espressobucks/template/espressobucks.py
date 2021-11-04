def solve(n: int, m: int, grid: list[list[chr]]) -> list[list[chr]]:
    return None

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    answer = solve(n, m, grid)
    for row in answer:
        print(''.join(row))