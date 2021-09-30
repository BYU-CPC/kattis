# (x, y) is the target destination
# n is the length of instructions
# instructions is a list of "Left" "Forward" and "Right"
# Do not return anything: print the line number and correct instruction 
def solve(x: int, y: int, n: int, instructions: list[str]) -> None:
    pass

if __name__ == '__main__':
    x, y = map(int, input().split())
    n = int(input())
    instructions = [input() for _ in range(n)]
    solve(x, y, n, instructions)