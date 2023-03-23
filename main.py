name_row_file = 'ZF_1_dug_lic_part_3_t.nc'

blocks = []
block = 1
file = open(name_row_file, 'r')
count = 1
for row_line in file:
    flag = ''
    if row_line.startswith('G0'):
        blocks.append(block)
        block = []
        block.append(row_line)
        flag = 'G0'
    elif row_line.startswith('G1'):
        blocks.append(block)
        block = []
        block.append(row_line)
        flag = 'G1'
    elif row_line.startswith('G2'):
        blocks.append(block)
        block = []
        block.append(row_line)
        flag = 'G2'
    elif row_line.startswith('G3'):
        blocks.append(block)
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

print(blocks)