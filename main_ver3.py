name_row_file = 'ZF_1_dug_lic_part_3_t.nc' #Имя файла с nc кодом для переработки

blocks = {} #Словарь, содержащий по ключу команды и номера строк - блок кода в виде списка строк
file = open(name_row_file, 'r')

count = 1 #Счетчик строк
flag = '' #Флаг для определяющий длящуюся команду


for row_line in file:
    if row_line.startswith('G0'):
        start_count = count - len(block)
        key = flag + ': ' + str(start_count) + ' - ' + str(count-1)
        blocks[key] = block
        block = []
        block.append(row_line)
        flag = 'G0'
    elif row_line.startswith('G1'):
        if 'block' in locals():
            start_count = count - len(block)
            key = flag + ': ' + str(start_count) + ' - ' + str(count-1)
            blocks[key] = block
            block = []
            block.append(row_line)
            flag = 'G1'
        else:
            block = []
            block.append(row_line)
            flag = 'G1'
    elif row_line.startswith('G2'):
        start_count = count - len(block)
        key = flag + ': ' + str(start_count) + ' - ' + str(count-1)
        blocks[key] = block
        block = []
        block.append(row_line)
        flag = 'G2'
    elif row_line.startswith('G3'):
        start_count = count - len(block)
        key = flag + ': ' + str(start_count) + ' - ' + str(count-1)
        blocks[key] = block
        block = []
        block.append(row_line)
        flag = 'G3'
    else :
        if row_line.startswith('M'):
            pass
        elif row_line.startswith('S'):
            pass
        elif row_line.startswith('('):
            pass
        else:
            block.append(row_line)
    
    count += 1        

# print(blocks.keys())
# for key in blocks.keys():
#         print(key,':', len(blocks[key]))
# test_out_file_name = 'test_out.nc'


def merge_into_logical_blocks(blocks:dict, row_limit:int = 2000):
    """Функция анализирует блоки кода, до ограничивающей строки - по умолчанию 2000 строк.
    Если блок содержащий G1 меньше 4х строк, он объединяется с блоком G2 или G3 выше по строкам, 
    а следующий за ним G2 или G3 блок объединяется с ними"""

    for key in blocks.keys():
        key_list = key.split()
        if  key_list[0][:-1] == 'G1' and  int(key_list[len(key_list)-1]) < row_limit: 
            if len(blocks[key]) < 4:
                print(key)


merge_into_logical_blocks(blocks)