from math import ceil

q, m, s, l = map(int, input().split())
height = ceil(l/m) * q          # how many rows of height q we have to have
if l % m:                       # if you partially filled a row with q's
    spots = (m - (l % m)) * q
    s = max(0, s - spots)       # fill in everything you can with those extra ones
height += ceil(s/m)
print(height)