from math import sqrt, acos
# есть координаты отрезков в виде котртежей, координаты начала отрезка и конца отрезка
#Нужно найти угол между отрезками

def angle(a, b):
    a_start_x, a_start_y, a_end_x, a_end_y = a
    b_start_x, b_start_y, b_end_x, b_end_y = b
    # Вычислить длину отрезка а 
    a_length = sqrt((a_end_x - a_start_x)**2 + (a_end_y - a_start_y)**2)
    b_length = sqrt((b_end_x - b_start_x)**2 + (b_end_y - b_start_y)**2)
    c_length = sqrt((a_end_x - b_end_x)**2 + (a_end_y - b_end_y)**2)
    angle_rad = acos((a_length**2 + b_length**2 - c_length**2) / (2 * a_length * b_length))
    angle_grad = angle_rad * 180 / 3.141592653589793
    return angle_grad


a = (0, 1000, 331.9743, 253.0507)
b = (0, 1000, 731.4518, 628.6275)

# I - вектор по оси X
# K - вектор по оси Z
text = ['X60.72 Z-38.414','G2 X17.558 Z-54.295 I226.314 K-681.704']
data_dict = {}
vc = []
for line in text:
    if line.startswith('G2'):
        line_list = line.split()
        for i in line_list:
            if i.startswith('X'):
                x = float(i[1:])
                data_dict['X2_end'] = x
            elif i.startswith('Z'):
                z = float(i[1:])
                data_dict['Z2_end'] = z
            elif i.startswith('I'):
                i = float(i[1:])
                vc.append(i)
            elif i.startswith('K'):
                k = float(i[1:])
                vc.append(k)
    else:
        if line.startswith('X'):
            x = float(line[1:])
            data_dict['X1_end'] = x
        elif line.startswith('Z'):
            z = float(line[1:])
            data_dict['Z1_end'] = z

X_start = data_dict['X1_end'] + vc[0]
Z_start = data_dict['Z1_end'] + vc[1]
data_dict['X1_start'] = X_start
data_dict['Z1_start'] = Z_start

print(angle(a, b))

