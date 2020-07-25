# https://open.kattis.com/problems/cups

n = int(input())

cols = []
rads = []

for _ in range(n):
    [a, b] = input().split(' ')
    if a.isnumeric():
        rads.append(int(a)/2)
        cols.append(b)
    else:
        rads.append(int(b))
        cols.append(a)

for idx in sorted(range(len(rads)), key= lambda k: rads[k]):
    print(cols[idx])
