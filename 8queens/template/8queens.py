def is_valid(board: list[list[str]]) -> bool:
    return False

if __name__ == '__main__':
    board = [list(input()) for _ in range(8)]
    print('valid' if is_valid(board) else 'invalid')