# a, b, and c are positive integers
# return True if they form a right triangle
# return False otherwise
def is_right_triangle(a: int, b: int, c: int) -> bool:
    return False

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    while a + b + c:
        print('right' if is_right_triangle(a, b, c) else 'wrong')
        a, b, c = map(int, input().split())