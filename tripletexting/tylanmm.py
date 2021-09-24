s = input()
l = len(s)//3
lst = [s[:l], s[l:2*l], s[2*l:]]
print(lst[0] if lst.count(lst[0]) > 1 else lst[1])