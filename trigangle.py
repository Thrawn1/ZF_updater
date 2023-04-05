from math import cos, sin, atan2, sqrt, pi
from matplotlib import pyplot as plt
print(pi)
Xa = 16.0
Ya = -41.2622

Xb = 255.9354
Yb = -718.2313

r = 718.2313
angle_rad = 0.016707709619449892 # противолежащий основанию угол в радианах

dx1 = Xa - Xb
dx1 = round(dx1, 4)
dy1 = Ya - Yb
dy1 = round(dy1, 4)
dx2 = dx1*cos(angle_rad) + dy1*sin(angle_rad)
dx2 = round(dx2, 4)
dy2 = -dx1*sin(angle_rad) + dy1*cos(angle_rad)
dy2 = round(dy2, 4)
Xc = Xb + dx2
Xc = round(Xc, 4)
Yc = Yb + dy2
Yc = round(Yc, 4)
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

x3 = Xc
y3 = Yc

I_new = Xb-x3
K_new = Yb-y3
I_new = round(I_new, 4)
K_new = round(K_new, 4)
print(I_new, K_new)
plt.show()
#Визуализировать точку (Xc, Yc)
