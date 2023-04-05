import math

penultimate_point = { 'x': 21.4832, 'y': 19.8919 }
circle = { 'x': 255.9354, 'y': -718.2313, 'r': 718.2313 }

def is_on_segment(start_x, start_y, end_x, end_y, x_intersect, y_intersect):
    """
    Проверяет, находится ли точка пересечения на заданном отрезке.
    """
    # Проверяем, что точка лежит на прямой, проходящей через начало и конец отрезка
    if ((x_intersect - start_x) * (end_y - start_y) - (y_intersect - start_y) * (end_x - start_x)) != 0:
        return False

    # Проверяем, что точка пересечения лежит на отрезке
    if (x_intersect < min(start_x, end_x) or x_intersect > max(start_x, end_x) or
            y_intersect < min(start_y, end_y) or y_intersect > max(start_y, end_y)):
        return False

    return True



# Известные данные
center_x = circle["x"]  # координата центра окружности по оси X
center_y = circle["y"]  # координата центра окружности по оси Y
radius = circle["r"]    # радиус окружности
start_x = penultimate_point["x"]   # координата начала отрезка по оси X
start_y = penultimate_point["y"]   # координата начала отрезка по оси Y
end_x = circle["x"]     # координата конца отрезка по оси X
end_y = circle["y"]     # координата конца отрезка по оси Y

# Вычисляем параметры прямой, проходящей через начало и конец отрезка
line_slope = (end_y - start_y) / (end_x - start_x) if end_x != start_x else math.inf
line_intercept = start_y - line_slope * start_x if line_slope != math.inf else start_x

# Вычисляем координаты точек пересечения прямой и окружности
a = 1 + line_slope ** 2
b = -2 * center_x + 2 * line_slope * (line_intercept - center_y)
c = center_x ** 2 + (line_intercept - center_y) ** 2 - radius ** 2

discriminant = b ** 2 - 4 * a * c
print(discriminant)

if discriminant < 0:
    print("Отрезок не пересекает окружность")
elif discriminant == 0:
    x_intersect = -b / (2 * a)
    y_intersect = line_slope * x_intersect + line_intercept
    if is_on_segment(start_x, start_y, end_x, end_y, x_intersect, y_intersect):
        print(f"Одна точка пересечения: ({x_intersect}, {y_intersect})")
    else:
        print("Отрезок не пересекает окружность")
else:
    x_intersect1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x_intersect2 = (-b - math.sqrt(discriminant)) / (2 * a)
    y_intersect1 = line_slope * x_intersect1 + line_intercept
    y_intersect2 = line_slope * x_intersect2 + line_intercept
    if is_on_segment(start_x, start_y, end_x, end_y, x_intersect1, y_intersect1):
        if is_on_segment(start_x, start_y, end_x, end_y, x_intersect2, y_intersect2):
            print(f"Две точки пересечения: ({x_intersect1}, {y_intersect1}), ({x_intersect2}, {y_intersect2})")
        else:
            print(f"Одна точка пересечения: ({x_intersect1}, {y_intersect1})")
    elif is_on_segment(start_x, start_y, end_x, end_y, x_intersect2, y_intersect2):
        print(f"Одна точка пересечения: ({x_intersect2}, {y_intersect2})")
    else:
        print('ddd')
        print("Отрезок не пересекает окружность")


