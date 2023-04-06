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
    
    start_line_1,end_line_1 = line_1
    start_line_2, end_line_2 = line_2
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

def arc_end_safety_angle(text:str, length_arc_safety:float) -> float:
    data_information = {}
    for line in text:
        parse_line_command(line,data_information)
    X_start = data_information['X1_end'] + data_information['I']
    Z_start = data_information['Z1_end'] + data_information['K']
    data_information['X_start'] = X_start
    data_information['Z_start'] = Z_start
    a_start = (data_information['X_start'], data_information['Z_start'], data_information['X1_end'], data_information['Z1_end'])
    b_end  = (data_information['X_start'], data_information['Z_start'], data_information['X2_end'], data_information['Z2_end'])
    arc_full_angl,R = calculate_angle_between_line(a_start, b_end)
    length_full_arc = 2 * pi * R / 360 * arc_full_angl
    data_information['length_full_arc'] = length_full_arc
    data_information['length_arc_safety'] = length_arc_safety
    safety_angle_arc_deg = length_arc_safety*360/(2 * pi * R)
    safety_angle_arc_rad = safety_angle_arc_deg * pi / 180
    data_information['safety_angle_arc_deg'] = safety_angle_arc_deg
    data_information['safety_angle_arc_rad'] = safety_angle_arc_rad
    return data_information