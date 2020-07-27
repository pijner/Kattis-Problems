# https://open.kattis.com/problems/artichoke

p, a, b, c, d, n = list(map(int, input().split()))

def price(k:int):
    from math import sin, cos
    return p * (sin(a*k + b) + cos(c*k + d) + 2)


stocks = list(map(price, list(range(1, n+1))))

currentMax = stocks[0]
largestDrop = 0
for s in stocks:
    change = currentMax - s
    if change > largestDrop:
        largestDrop = change
    if s > currentMax:
        currentMax = s

print(largestDrop)