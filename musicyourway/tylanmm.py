attrs = {a: i for i, a in enumerate(input().split())}
songs = [input().split() for _ in range(int(input()))]
for _ in range(int(input())):
    print(' '.join(attrs.keys()))
    attr = input()
    songs.sort(key=lambda x: x[attrs[attr]])
    print('\n'.join([' '.join(song) for song in songs]))
    print()