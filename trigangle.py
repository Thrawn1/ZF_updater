from math import cos, sin, atan2, sqrt, pi
from matplotlib import pyplot as plt
from work_arc import calculate_length_line, calculate_angle_between_line, parse_line_command, arc_end_safety_angle


def calculate_coordinates_end_safety_arc(data_information:dict) -> tuple:
    """Функция вычисляет координаты конца безопасной дуги."""
    angle_safety_arc = data_information['safety_angle_arc_rad']
    delta_x_axe_1 = data_information['X2_end'] - data_information['X_centr_arc']
    delta_z_axe_1 = data_information['Z2_end'] - data_information['Z_centr_arc']
    delta_x_axe_2 = delta_x_axe_1*cos(angle_safety_arc) + delta_z_axe_1*sin(angle_safety_arc)
    delta_z_axe_2 = -delta_x_axe_1*sin(angle_safety_arc) + delta_z_axe_1*cos(angle_safety_arc)
    xsa = data_information['X_centr_arc'] + delta_x_axe_2
    zsa = data_information['Z_centr_arc'] + delta_z_axe_2
    data_information['X_safety_arc_end'] = xsa
    data_information['Z_safety_arc_end'] = zsa
    return (xsa, zsa),data_information


def calculate_vector_center_arc(data_information:dict) -> tuple:
    print(data_information)
    I_safety_arc_raw = data_information['X_centr_arc'] - data_information['X_safety_arc_end']
    K_sefety_arc_raw = data_information['Z_centr_arc'] - data_information['Z_safety_arc_end']
    I_safety_arc = round(I_safety_arc_raw,4)
    K_sefety_arc = round(K_sefety_arc_raw,4)
    print(I_safety_arc,K_sefety_arc)
    return (I_safety_arc,K_sefety_arc)

def build_text_command(data_information:dict,vec:tuple) -> list:
    list_text = []
    line_1 = 'G1 ' + 'X' + str(data_information['X1_end']) + ' ' + 'Z' + str(data_information['Z1_end']) + ' F30'
    print(line_1)
    list_text.append(line_1)
    line_2 = 'G' + str(data_information['G']) + ' ' + 'X' + str(round((data_information['X_safety_arc_end']),4)) + ' ' + 'Z' + str(round((data_information['Z_safety_arc_end']),4)) + ' ' + 'I' + str(data_information['I']) + ' ' + 'K' + str(data_information['K']) + ' F3000'
    print(line_2)
    list_text.append(line_2)
    line_3 = 'X' + str(round((data_information['X2_end']),4)) + ' ' + 'Z' + str(round((data_information['Z2_end']),4)) + ' ' + 'I' + str(vec[0]) + ' ' + 'K' + str(vec[1]) + ' F30'
    print(line_3)
    list_text.append(line_3)
text = ['X495.8709 Z-41.2622','G2 X16.0  Z-41.2622 I-239.9355 K-676.9691']
t = arc_end_safety_angle(text, 12)
print(t)
o,yy = calculate_coordinates_end_safety_arc(t)
print(o)
tt = calculate_vector_center_arc(yy)
build_text_command(yy,tt)

#Визуализация
# plt.axes().set_aspect('equal')
# plt.xlim(-500, 1100)
# plt.ylim(-1700, 100)
# plt.plot(Xb, Yb, 'ro')
# circle = plt.Circle((Xb, Yb), r, color='r', fill=False)
# plt.gcf().gca().add_artist(circle)
# plt.plot([Xa, Xb, Xc, Xa], [Ya, Yb, Yc, Ya], 'ro-')
# plt.show()

