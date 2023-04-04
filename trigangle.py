from math import cos, sin, atan2, sqrt, pi
from matplotlib import pyplot as plt

Xa = 17.558
Ya = -54.295

Xb = 287.034
Yb = -711.118

r = 718.2885 
angle_rad = 0.016706379122038012 # противолежащий основанию угол в радианах

dx1 = Xa - Xb
dy1 = Ya - Yb
dx2 = dx1*cos(angle_rad) + dy1*sin(angle_rad)
dy2 = -dx1*sin(angle_rad) + dy1*cos(angle_rad)
Xc = Xb + dx2
Yc = Yb + dy2
print( 'Xc = ', Xc, 'Yc = ', Yc)

#Визуализировать окружность радиусом r и центром в точке (Xb, Yb)
plt.axes().set_aspect('equal')
plt.plot(Xb, Yb, 'ro')
circle = plt.Circle((Xb, Yb), r, color='r', fill=False)
plt.gcf().gca().add_artist(circle)
#Визуализировать треугольник
plt.plot([Xa, Xb, Xc, Xa], [Ya, Yb, Yc, Ya], 'ro-')
plt.show()
#Визуализировать точку (Xc, Yc)
