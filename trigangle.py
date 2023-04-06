from math import cos, sin, atan2, sqrt, pi
from matplotlib import pyplot as plt
from work_arc import calculate_length_line, calculate_angle_between_line, parse_line_command, arc_end_safety_angle

#Входные данные 


Xa = 16.0
Ya = -41.2622
Xb = 255.9354
Yb = -718.2313
r = 718.2313
angle_rad = 0.016707709619449892 # противолежащий основанию угол в радианах


def calculate_coordinates_end_safety_arc(data_information:dict) -> tuple:
    """Функция вычисляет координаты конца безопасной дуги."""

    delta_x_axe_1 = round((data_information['X2_end'] - data_information['X_centr_arc']),4)
    delta_z_axe_1 = round((data_information['Z2_end'] - data_information['Z_centr_arc']),4)
    delta_x_axe_2 = round((delta_x_axe_1*cos(angle_rad) + delta_z_axe_1*sin(data_information['safety_angle_arc_rad'])),4)
    delta_z_axe_2 = round((-delta_x_axe_1*sin(angle_rad) + delta_z_axe_1*cos(angle_rad)),4)
    xsa = round((data_information['X_centr_arc'] + delta_x_axe_2),4)
    zsa = round((data_information['Z_centr_arc'] + delta_z_axe_2),4)
    print( 'X_safety_arc_end = ', xsa, 'Z_safety_arc_end = ', zsa)
    return (xsa, zsa)


def calculate_vector_center_arc(data_information:dict) -> tuple:
    pass


text = ['X495.8709 Z-41.2622','G2 X16.0  Z-41.2622 I-239.9355 K-676.9691']
t = arc_end_safety_angle(text, 12)
print(t)
o = calculate_coordinates_end_safety_arc(t)
print(o)
    # x3 = Xc
    # y3 = Yc
    # I_new = Xb-x3
    # K_new = Yb-y3
    # I_new = round(I_new, 4)
    # K_new = round(K_new, 4)
    # print(I_new, K_new)


#Визуализация
# plt.axes().set_aspect('equal')
# plt.xlim(-500, 1100)
# plt.ylim(-1700, 100)
# plt.plot(Xb, Yb, 'ro')
# circle = plt.Circle((Xb, Yb), r, color='r', fill=False)
# plt.gcf().gca().add_artist(circle)
# plt.plot([Xa, Xb, Xc, Xa], [Ya, Yb, Yc, Ya], 'ro-')
# plt.show()

