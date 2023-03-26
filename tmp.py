name_file_1 = 'test_out_5.nc'
name_file_2 = 'ZF_1_dug_lic_part_3_t.nc'

file_1 = open(name_file_1, 'r')
file_2 = open(name_file_2, 'r')
count = 1
for line_1 in file_1:
    line_2 = file_2.readline()
    if line_1 != line_2:
        print('Строка', count)
        print(line_1)
        print(line_2)
        print('-----------------')
        break
    count += 1