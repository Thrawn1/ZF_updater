class State:
    def __init__(self):
        self.command_type = -1
        self.x = 0
        self.y = 0
        self.z = 0
        self.feed = 0
        self.rpm = 0
        self.direction = 0

        
class Blank:
    def __init__(self, width, height, length):
        self.width = 0
        self.height = 0
        self.length = 0
        self.x_start = 0
        self.y_start = 0
        self.z_start = 0

    def get_direction(self,x_now):
        center_blank = self.x_start + self.width/2
        if x_now > center_blank:
            self.direction = 0
        else:
            self.direction = 1
        return self.direction



# Открыть файл с командами
# Перебрать команды
# Если строка начинается с '(' - сторока игнорируется
# Если строка начинается с 'G0' - движение холостого хода . Нужно запомнить что команда началась 
# Если строка начинается с 'G1' - движение вперед. Нужно запомнить что команда началась 
# Если строка начинается с 'G2' - движение по дуге. Нужно запомнить что команда началась
# Если строка начинается с 'G3' - движение по дуге. Нужно запомнить что команда началась
# Если строка начинается с 'S' - ключ оборотов двигателя
# Если строка начинается с 'F' - ключ скорости движения. 

name_row_file = 'ZF_1_dug_lic_part_3.nc'

width = 577
height = 104
length = 476

blank = Blank(width, height, length)
state_adapter = State()


# Открыть файл с командами
file = open(name_row_file, 'r')

for line_row in file: 
    line_list = line_row.split()
    line = line_list[0]
    if line.startswith('('):
        continue
    elif line.startswith('G0'):
        state_adapter.command_type = 0
    elif line.startswith('G1'):
        state_adapter.command_type = 1
    elif line.startswith('G2'):
        state_adapter.command_type = 2
    elif line.startswith('G3'):
        state_adapter.command_type = 3
    elif line.startswith('S'):
        state_adapter.rpm = line[1:]
    elif line.startswith('F'):
        state_adapter.feed = line[1:]
    elif line.startswith('X'):
        state_adapter.x = line[1:]
    elif line.startswith('Y'):
        state_adapter.y = line[1:]
    elif line.startswith('Z'):
        state_adapter.z = line[1:]
    else:
        continue
