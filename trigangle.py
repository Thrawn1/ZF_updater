from math import cos, sin, atan2, sqrt, pi
from matplotlib import pyplot as plt

Xa = 16
Ya = -41.2622

Xb = 255.9354
Yb = -718.2313

r = 718.2313
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
plt.xlim(-500, 1100)
plt.ylim(-1700, 100)
plt.plot(Xb, Yb, 'ro')
circle = plt.Circle((Xb, Yb), r, color='r', fill=False)
plt.gcf().gca().add_artist(circle)
#Визуализировать треугольник
plt.plot([Xa, Xb, Xc, Xa], [Ya, Yb, Yc, Ya], 'ro-')

x3 = 28.71
y3 = -49.889

I_new = Xb-x3
K_new = Yb-y3
print(I_new, K_new)
plt.show()
#Визуализировать точку (Xc, Yc)
