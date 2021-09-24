n = int(input())
passwords = []
for _ in range(n):
    password, prob = input().split()
    prob = float(prob)
    passwords.append((password, prob))
passwords.sort(key=lambda x:x[1], reverse=True)

# exp -> expected value, prob -> probability of first i passwords being wrong
exp, prob = 0, 1
for i in range(n):
    exp += (i+1) * passwords[i][1]
    prob *= 1 - passwords[i][1]
print(exp)