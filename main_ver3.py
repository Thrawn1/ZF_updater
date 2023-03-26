name_row_file = 'ZF_1_dug_lic_part_3_t.nc' #Имя файла с nc кодом для переработки


def check_merge_block(blocks:dict) -> dict:
    """Функция проверяет блоки кода на возможность объединения"""
    blocks_result = blocks.copy()
    blocks_merge = {}
    for key_1 in blocks.keys():
        key_list_1 = key_1.split()
        id_block_1 = int(key_list_1[0])
        for key_2 in blocks.keys():
            key_2_list = key_2.split()
            id_block_2 = int(key_2_list[0])
            diff = id_block_2 - id_block_1
            if 5 > diff > 0:
                if blocks[key_1][len(blocks[key_1])-1] == blocks[key_2][0]:
                    print(diff)
                    print('--------------------------------------------------')
                    print('KEY_1', key_1)
                    print(blocks[key_1])
                    print('--------------------------------------------------')
                    print('KEY_2', key_2)
                    print(blocks[key_2])
                    print('--------------------------------------------------')



                    if key_1 == '108 G3: 1768 - 1768':
                        print('Блоки', blocks[key_1], 'объединены')
                    blocks[key_2].pop(0)
                    blocks_result[key_2] = blocks[key_1] + blocks[key_2]
                    del blocks_result[key_1]
                    blocks_merge[key_1] = blocks[key_1]
    return blocks_result


def writing_keys(blocks:dict, name_file:str):
    """Функция записывает ключи словаря блоков кода в файл"""
    file = open(name_file, 'w')
    for key in blocks.keys():
        file.write(key + '\n')
    file.close()



def key_blocks_sort(key_block:list) -> list:
    temp_dict = {}
    for key in key_block:
        key_list = key.split()
        id_block = int(key_list[0])
        temp_dict[id_block] = key
    list_key = list(temp_dict.keys())
    list_key.sort()
    #print(list_key)
    new_key_block = []
    for key in list_key:
        new_key_block.append(temp_dict[key])
    return new_key_block







def writing_commands_to_file(blocks:dict, name_file:str):
    """Функция записывает блоки кода в файл"""
    file = open(name_file, 'w')
    list_key_raw = list(blocks.keys())
    list_key = key_blocks_sort(list_key_raw)
    for key_block in list_key:
        block = blocks[key_block]
        for row_line in block:
            file.write(row_line)
    file.close()



def clear_feed_in_row(row_line:str,id_row:int,row_limit:int = 2000) -> str:
    if 'F' in row_line:
        line_list = row_line.split()
        for command in line_list:
            if command.startswith('F'):
                feed = int(command[1:])
                if feed == 1000:
                    if id_row > row_limit:
                        return line_row
                    else:
                        line_list.remove(command)
                        line_row = ' '.join(line_list)
                        line_row = line_row + '\n'
                        return line_row
                elif feed == 90:
                    print('ПРЕДУПРЕЖДЕНИЕ!')
                    print('В строке', id_row, 'подача равна 90')
                    #Заменить подачу с 90 на 10 
                    line_list.remove(command)
                    line_row = ' '.join(line_list)
                    line_row = line_row + '\n'
                    return line_row
                else:
                    line_list.remove(command)
                    line_row = ' '.join(line_list)
                    line_row = line_row + '\n'
                    return line_row
    else:
        return row_line




def clear_feed(blocks:dict, row_limit:int = 2000) -> dict:
    new_blocks = blocks.copy()
    for key_block in blocks.keys():
        block = blocks[key_block]
        key_list = key_block.split()
        end_row = int(key_list[len(key_list)-1])
        len_block = len(block)
        id_row = end_row - len_block
        new_blick = []
        for row_line in block:
            new_line = clear_feed_in_row(row_line,id_row,row_limit)
            new_blick.append(new_line)
            id_row += 1
        del new_blocks[key_block]
        new_blocks[key_block] = new_blick
    return new_blocks

            
            
def set_feed(blocks:dict, row_limit:int = 2000) -> dict:
    step = len(blocks.keys())
    print(step)
    key_list_raw = list(blocks.keys())
    key_list = key_blocks_sort(key_list_raw)
    for key_block in key_list:
        print(key_block)



def write_block_to_blocks(block:list, blocks:dict, count:int, flag:str):
    """Функция записывает блок кода в словарь блоков кода"""
    a = len(block)
    start_count = count - a
    key = str(c_block) + ' ' +  flag + ': ' + str(start_count) + ' - ' + str(count-1)
    blocks[key] = block
    block = []
    return blocks, block



def merge_into_logical_blocks(blocks:dict, row_limit:int = 2000):
    """Функция анализирует блоки кода, до ограничивающей строки - по умолчанию 2000 строк.
    Если блок содержащий G1 меньше 4х строк, он объединяется с блоком G2 или G3 выше по строкам, 
    а следующий за ним G2 или G3 блок объединяется с ними"""


    blocks_merge = {}
    blocks_new = blocks.copy()
    for i in range(len(blocks_new.keys())):
        if i >= len(blocks_new.keys()):
            break
        keys_sorted = key_blocks_sort(list(blocks_new.keys()))
        key = list(keys_sorted)[i]

        key_list = key.split()
        if  key_list[1][:-1] == 'G1' and  int(key_list[len(key_list)-1]) < row_limit: 
            if len(blocks_new[key]) < 5:
                #print(key)
                if i < len(blocks_new.keys()):
                    next_key = keys_sorted[i+1]
                else:
                    next_key = key
                prev_key = keys_sorted[i-1]
                new_block = blocks_new[prev_key] + blocks_new[key] + blocks_new[next_key]
                try:
                    del blocks_new[prev_key]
                    i-=1
                except:
                    print("Oops")
                
                del blocks_new[key]
                i-=1

                del blocks_new[next_key]
                i-=1
                
                prev_key_list = prev_key.split()
                next_key_list = next_key.split()
                new_key = f"{prev_key_list[0]} {prev_key_list[1]} {prev_key_list[2]} - {next_key_list[4]}"
                blocks_new[new_key] = new_block
                i+=1
    return blocks_new




blocks = {} #Словарь, содержащий по ключу команды и номера строк - блок кода в виде списка строк
file = open(name_row_file, 'r')

count = 1 #Счетчик строк
flag = '' #Флаг для определяющий длящуюся команду

c_block = 1 #Счетчик блоков
for row_line in file:
    if row_line.startswith('G0'):
        blocks, block = write_block_to_blocks(block, blocks, count, flag)
        block.append(row_line)
        flag = 'G0'
        c_block += 1
    elif row_line.startswith('G1'):
        if 'block' in locals():
            blocks, block = write_block_to_blocks(block, blocks, count, flag)
            block.append(row_line)
            flag = 'G1'
            c_block += 1
        else:
            block = []
            block.append(row_line)
            flag = 'G1'
    elif row_line.startswith('G2'):
        blocks, block = write_block_to_blocks(block, blocks, count, flag)
        block.append(row_line)
        flag = 'G2'
        c_block += 1
    elif row_line.startswith('G3'):
        blocks, block = write_block_to_blocks(block, blocks, count, flag)
        block.append(row_line)
        flag = 'G3'
        c_block += 1
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

# file_name_key = 'keys.txt'
# writing_keys(blocks, file_name_key)
# print(blocks['102 G2: 1747 - 1748'])
#print(blocks.keys())
# for key in blocks.keys():
#         print(key,':', len(blocks[key]))
# test_out_file_name = 'test_out.nc'
key_0 = '1 G1: 5 - 5'
del blocks[key_0]
blocks_temp = merge_into_logical_blocks(blocks)
blocks_t = merge_into_logical_blocks(blocks_temp)
# for key_m in blocks_m.keys():
#     print('------------------')
#     print('Ключ: ',key_m)
#     print('Результат слияния: \n',blocks_m[key_m])
#     print('------------------')
# print('------------------')
# print(len(blocks_m.keys()))
# print('------------------')
# print('------------------')
# print('------------------')
# a = check_merge_block(blocks_m)
# for key_am in a.keys():
#     print('------------------')
#     print('Ключ: ',key_am)
#     print('Результат слияния: \n',a[key_am])
#     print('------------------')
# print(len(a.keys()))
# for key in blocks_t.keys():
#     print(key)
#print(blocks_t['26 G3: 396 - 397'])
file_output_name = 'test_out_v_6.nc'
#clear_blocks = clear_feed(blocks_t)
writing_commands_to_file(blocks_t, file_output_name)
#set_feed(blocks_t)