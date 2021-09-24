def factorial(n):
    end = n
    for i in range(2, n):
        end *= i
    return end

for i in range(int(input())):
    print(str(factorial(int(input())))[-1])