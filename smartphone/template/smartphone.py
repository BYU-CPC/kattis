# target is the word you want to type
# written is what has been written so far
# suggestions contains the three suggestion strings
# return the minimum number of keypresses needed
def min_keypresses(target: str, written: str, suggestions: list[str]) -> int:
    return 0

if __name__ == '__main__':
    for _ in range(int(input())):
        target = input()
        written = input()
        suggestions = [input() for _ in range(3)]
        print(min_keypresses(target, written, suggestions))