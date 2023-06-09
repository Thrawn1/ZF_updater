from math import sqrt, acos,pi

def calculate_length_line(start:tuple, end:tuple, flag = 0) -> float:
    """Функция вычисляет длину отрезка по координатам его концов."""
    
    x1, y1 = start
    x2, y2 = end
    length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if flag != 0:
        return length
    else:
        return round(length, 4)   

def calculate_angle_between_line(line_1:tuple, line_2:tuple) -> float:
    """Функция вычисляет угол между двумя отрезками по координатам их концов."""
    
    start_line_1,end_line_1 = (line_1[0],line_1[1]), (line_1[2],line_1[3])
    start_line_2,end_line_2 = (line_2[0],line_2[1]), (line_2[2],line_2[3])
    start_line_3 = end_line_1
    end_line_3 = end_line_2
    length_line_1 = calculate_length_line(start_line_1, end_line_1,1)
    length_line_2 = calculate_length_line(start_line_2, end_line_2,1)
    length_line_3 = calculate_length_line(start_line_3, end_line_3,1)
    angle_between_line_rad   = acos((length_line_1 + length_line_2 - length_line_3**2) / (2 * length_line_1 * length_line_2))
    return angle_between_line_rad

def parse_line_command(line:str,data_information: dict) -> tuple:
    """Функция парсит строку с командой и возвращает словарь с данными и список с векторами смещения."""

    if line.startswith('G2'):
        line_list = line.split()
        for i in line_list:
            data_information['G'] = 2
            if i.startswith('X'):
                x = float(i[1:])
                data_information['X2_end'] = x
            elif i.startswith('Z'):
                z = float(i[1:])
                data_information['Z2_end'] = z
            elif i.startswith('I'):
                i = float(i[1:])
                data_information['I'] = i
            elif i.startswith('K'):
                k = float(i[1:])
                data_information['K'] = k
    else:
        line_list = line.split()
        for i in line_list:
            if i.startswith('X'):
                x = float(i[1:])
                data_information['X1_end'] = x
            elif i.startswith('Z'):
                z = float(i[1:])
                data_information['Z1_end'] = z
    return data_information

def get_radius_arc(x_center:float, y_center:float, x_end:float, y_end:float) -> float:
    """Функция вычисляет радиус дуги по координатам центра дуги и ее начала."""    
    
    radius = calculate_length_line((x_center, y_center), (x_end, y_end))
    return radius

def convert_rad_to_grad(angle_rad:float):
    angle_grad = (180*angle_rad)/pi
    return angle_grad

def arc_end_safety_angle(text:list, length_arc_safety:float) -> float:
    
    data_information = {}
    for line in text:
        parse_line_command(line,data_information)
    X_start = data_information['X1_end'] + data_information['I']
    Z_start = data_information['Z1_end'] + data_information['K']
    data_information['X_centr_arc'] = X_start
    data_information['Z_centr_arc'] = Z_start
    border_line_start_arc = (data_information['X_centr_arc'], data_information['Z_centr_arc'], data_information['X1_end'], data_information['Z1_end'])
    border_line_end_arc  = (data_information['X_centr_arc'], data_information['Z_centr_arc'], data_information['X2_end'], data_information['Z2_end'])
    arc_full_angl = calculate_angle_between_line(border_line_start_arc, border_line_end_arc)
    r = get_radius_arc(data_information['X_centr_arc'], data_information['Z_centr_arc'], data_information['X1_end'], data_information['Z1_end'])
    data_information['radius_arc'] = r
    arc_full_angl_grad = convert_rad_to_grad(arc_full_angl)
    print(arc_full_angl)
    length_full_arc = 2 * pi * r / 360 * arc_full_angl_grad
    print('Угол дуги: ',arc_full_angl_grad)
    data_information['length_full_arc'] = length_full_arc
    data_information['length_arc_safety'] = length_arc_safety
    safety_angle_arc_deg = length_arc_safety*360/(2 * pi * r)
    safety_angle_arc_rad = safety_angle_arc_deg * pi / 180
    data_information['safety_angle_arc_deg'] = safety_angle_arc_deg
    data_information['safety_angle_arc_rad'] = safety_angle_arc_rad
    return data_information