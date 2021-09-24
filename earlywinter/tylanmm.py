n, d = map(int, input().split())
count = 0
for num in map(int, input().split()):
    if num <= d:
        print(f'It hadn\'t snowed this early in {count} years!')
        break
    count += 1
else:
    print('It had never snowed this early!')