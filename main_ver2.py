name_row_file = 'ZF_1_dug_lic_part_3.nc'

width = 577
height = 104
length = 476
file  = open(name_row_file, 'r')
count = 0
for row_line in file: 
    if row_line.startswith('('):
        continue
    elif row_line.startswith('G0'):
        print('G0')
    elif row_line.startswith('G1'):
        print('G1')
    elif row_line.startswith('G2'):
        print('G2')
    elif row_line.startswith('G3'):
        print('G3')
    else:
        if 'I' in row_line or 'K' in row_line:
            print('I/K')
        elif 'X' in row_line or 'Y' in row_line or 'Z' in row_line:
            print('X/Y/Z')
        else:
            continue
    count += 1
        