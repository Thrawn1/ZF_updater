from math import sqrt, acos
# есть координаты отрезков в виде котртежей, координаты начала отрезка и конца отрезка
#Нужно найти угол между отрезками

def angle(a, b):
    a_start_x, a_start_y, a_end_x, a_end_y = a
    b_start_x, b_start_y, b_end_x, b_end_y = b
    # Вычислить угол между отрезками
    c_start_x = a_start_x - b_start_x


a = (0, 1000, 331.9743, 253.0507)
b = (0, 1000, 731.4518, 628.6275)
print(angle(a, b))