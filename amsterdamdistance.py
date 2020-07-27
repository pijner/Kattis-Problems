# https://open.kattis.com/problems/amsterdamdistance

from math import pi

m, n, r = list(map(float, input().split()))
m = int(m)
n = int(n)

ax, ay, bx, by = list(map(int, input().split()))
ROAD_LENGTH = r/n

def arcLength(ring:int):
    return pi * r * ring / (n * m)


numRoads = by - ay
numArcs = bx - ax
dist = 0
roadOnlyDist = 2*r
if numRoads == 0:
    roadOnlyDist = ay*2*ROAD_LENGTH
elif numArcs == 0:
    roadOnlyDist = abs(numRoads) * ROAD_LENGTH
else:
    roadOnlyDist = ROAD_LENGTH * (ay + by)

if numRoads < 0:
    dist = ROAD_LENGTH * abs(numRoads) + arcLength(by) * abs(numArcs)
else:
    dist = ROAD_LENGTH * abs(numRoads) + arcLength(ay) * abs(numArcs)


print(min(dist, roadOnlyDist))
