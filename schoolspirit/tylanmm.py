def calcScore(stu):
    score = 0
    for i in range(len(stu)):
        score += stu[i] * 0.8**i
    return 0.2*score

n = int(input())
students = [int(input()) for i in range(n)]
print(calcScore(students))

mean = 0
for i in range(n):
    curr = students.pop(i)
    mean += calcScore(students)
    students.insert(i, curr)
print(mean/n)