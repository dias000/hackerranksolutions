from math import degrees, atan2

AB = int(input())
BC = int(input())

res = round(degrees(atan2(AB, BC)))
print(str(res) + '°')

