for _ in range(int(input())):
    n = int(input())
    deck = []
    while n:
        deck.insert(0, str(n))
        for _ in range(n):
            deck.insert(0, deck.pop())
        n -= 1
    print(' '.join(deck))