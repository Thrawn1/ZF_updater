from math import sqrt, acos,pi

#Модуль надо переименовать
#Разбить функцию tmp_name на несколько функций. В частности - функцию вычисления радиуса дуги
#Функцию вычисления угла малой дуги окончания движения(что бы можно было передать в нее значения длины дуги окончания)
#Функцию-парсер строк с командами 
#Функцию-справку о дуге - радиус, длина, угол, начало, конец и т.д.

def angle(a, b):
    a_start_x, a_start_y, a_end_x, a_end_y = a
    b_start_x, b_start_y, b_end_x, b_end_y = b
    a_length = sqrt((a_end_x - a_start_x)**2 + (a_end_y - a_start_y)**2)
    b_length = sqrt((b_end_x - b_start_x)**2 + (b_end_y - b_start_y)**2)
    if round(a_length, 4) == round(b_length, 4):
        R = a_length
    else:
        print('Ошибка определения радиуса!')
        return 0,0
    c_length = sqrt((a_end_x - b_end_x)**2 + (a_end_y - b_end_y)**2)
    angle_rad = acos((a_length**2 + b_length**2 - c_length**2) / (2 * a_length * b_length))
    angle_grad = angle_rad * 180 / pi
    return angle_grad,R


def tmp_name(text):
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
            line_list = line.split()
            for i in line_list:
                if i.startswith('X'):
                    x = float(i[1:])
                    data_dict['X1_end'] = x
                elif i.startswith('Z'):
                    z = float(i[1:])
                    data_dict['Z1_end'] = z
    X_start = data_dict['X1_end'] + vc[0]
    Z_start = data_dict['Z1_end'] + vc[1]
    print(X_start, Z_start)
    data_dict['X_start'] = X_start
    data_dict['Z_start'] = Z_start
    a_start = (data_dict['X_start'], data_dict['Z_start'], data_dict['X1_end'], data_dict['Z1_end'])
    b_end  = (data_dict['X_start'], data_dict['Z_start'], data_dict['X2_end'], data_dict['Z2_end'])
    angl,R = angle(a_start, b_end)
    l_dug = 2 * pi * R / 360 * angl
    print('Радиус дуги: ', R) 
    print('lenght arc: ', l_dug)
    l_dug_secured = 12
    new_angl = l_dug_secured*360/(2 * pi * R)
    new_angl_rad = new_angl * pi / 180
    return new_angl_rad


text = ['X495.8709 Z-41.2622','G2 X16.0  Z-41.2622 I-239.9355 K-676.9691']
angl = tmp_name(text)
print(angl)