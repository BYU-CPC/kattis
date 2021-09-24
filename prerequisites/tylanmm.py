line = input()
while line != '0':
    k, m = map(int, line.split())
    courses = set(map(int, input().split()))
    reqMet = True
    for _ in range(m):
        l = list(map(int, input().split()))
        c, r, reqs = l[0], l[1], set(l[2:])
        reqMet &= len(courses.intersection(reqs)) >= r
    print('yes' if reqMet else 'no')
    line = input()