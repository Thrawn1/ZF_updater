name_row_file = 'ZF_1_dug_lic_part_3_t.nc'


def clear_feed(line_row,count: str) -> str:
    """Удаление подачи из строки кода"""
    if 'F' in line_row:
        line_list = line_row.split()
        for command in line_list:
            if 'F' in command:
                feed = int(command[1:])
                if feed == 1000:
                    if count >1200:
                        return line_row
                    else:
                        line_list.remove(command)
                        line_row = ' '.join(line_list)
                        line_row = line_row + '\n'
                        return line_row
                elif feed == 90:
                    #Заменить подачу с 90 на 10 
                    line_list.remove(command)
                    line_list.append('F10')
                    line_row = ' '.join(line_list)
                    line_row = line_row + '\n'
                    return line_row
                else:
                    line_list.remove(command)
                    line_row = ' '.join(line_list)
                    line_row = line_row + '\n'
                    return line_row
                    
    else:
        return line_row



def detect_block_feed(blocks: list,row_line: str,count: int) -> list:
    """Определение блока кода с подачей"""
    
    pass


width = 577
height = 104
length = 476
file  = open(name_row_file, 'r')
blocks = []
count = 1
for row_line in file: 
    if row_line.startswith('('):
        print(row_line)
    elif row_line.startswith('S'):
        print(row_line)
    elif row_line.startswith('G0'):
        new_line = clear_feed(row_line,count)
        print(new_line)
    elif row_line.startswith('G1'):
        new_line = clear_feed(row_line,count)
        print(new_line)
    elif row_line.startswith('G2'):
        new_line = clear_feed(row_line,count)
        print(new_line)
    elif row_line.startswith('G3'):
        new_line = clear_feed(row_line,count)
        print(new_line)
    else:
        if 'I' in row_line or 'K' in row_line:
            new_line = clear_feed(row_line,count)
            print(new_line)
        else:
            if 'M' not in row_line:
                new_line = clear_feed(row_line,count)
                print(new_line)
            else:  
                print(row_line)
    count += 1


