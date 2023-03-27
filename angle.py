from math import sqrt, acos
 
ax, ay, bx, by = map(int, input().split())
ma = sqrt(ax * ax + ay * ay)
mb = sqrt(bx * bx + by * by)
sc = ax * bx + ay * by
res = acos(sc / ma / mb)
print("{res}".format(res=round(res, 5)))