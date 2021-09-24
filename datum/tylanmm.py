d, m = map(int, input().split())
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = sum(months[:m-1]) + d
week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
print(week[(day-1) % 7])