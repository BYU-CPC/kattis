s, t, n = tuple(map(int, input().split()))
walkTimes = list(map(int, input().split()))[::-1]
rideTimes = list(map(int, input().split()))[::-1]
busTimes = list(map(int, input().split()))[::-1]

time = s
canMakeIt = True
while canMakeIt and len(busTimes) > 0:
    time += walkTimes.pop()
    nextBus = busTimes.pop()
    time += (nextBus - (time % nextBus)) % nextBus
    time += rideTimes.pop()

    if time >= t:
        canMakeIt = False

time += walkTimes.pop()
if time > t:
    canMakeIt = False

print("yes" if canMakeIt else "no")