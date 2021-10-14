# You will need to implement both of the following functions
def encode(message: str) -> str:
    return ''

def decode(message: str) -> str:
    return ''

if __name__ == '__main__':
    t, msg = input().split()
    print(encode(msg) if t == 'E' else decode(msg))