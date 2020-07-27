# https://open.kattis.com/problems/anothercandies

t = int(input())

while t:
    t -= 1
    _ = input()
    n = int(input())

    sum = 0
    for i in range(n):
        c = int(input())
        sum += c

    parts = sum % n
    print("YES") if parts == 0 else print("NO")
