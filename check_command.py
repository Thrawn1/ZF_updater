
circle = { 'x': 255.9354, 'y': -718.2313, 'r': 718.2313 }
end_point = { 'x': 16.0, 'y': -41.2622 }
start_point = { 'x': 495.8709, 'y': -41.2622 }
penultimate_point = { 'x': 27.3437, 'y': -37.348 }

#state 1
line_1 = f'G1 X{start_point["x"]} Z{start_point["y"]}'
#state 2
line_2 = f'G2 X{penultimate_point["x"]} Z{penultimate_point["y"]} I{start_point["x"]-circle["x"]} K{start_point["y"]-circle["y"]}'
#state 3
line_3 = f'G2 X{end_point["x"]} Z{end_point["y"]} I{penultimate_point["x"]-circle["x"]} K{penultimate_point["y"]-circle["y"]}'

print(line_1)
print(line_2)
print(line_3)

k = penultimate_point['x']*penultimate_point['x'] + penultimate_point['y']*penultimate_point['y'] - circle['r']*circle['r']
rr = circle['r']*circle['r']
print(k, rr)    