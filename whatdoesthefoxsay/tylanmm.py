for _ in range(int(input())):
    sounds = input().split()

    # find other animal sounds
    badSounds = set()
    line = input().split()
    while line[-1][-1] != '?':
        badSounds.add(line[-1])
        line = input().split()
    
    foxSounds = []
    for s in sounds:
        if s not in badSounds:
            foxSounds.append(s)
    print(' '.join(foxSounds))