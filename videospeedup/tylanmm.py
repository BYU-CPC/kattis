n, p, k = map(int, input().split())
times = [0] + list(map(int, input().split())) + [k]
time = times[1]
speed = 100
for i in range(1, n+1):
    speed += p
    time += (times[i+1] - times[i])*(speed/100)
print(time)