#!/usr/bin/python3
from starutils import startTest, printD, hasParam, getParam

lines = startTest()
total = 0

line = lines[0]

map = list()
files = list()
free_space = list()

def print_map():
	if hasParam("-d"):
		str_result = ""
		for l in map:
			if l == -1:
				str_result += "."
			else:
				str_result += str(l)
		printD(str_result)


valid_file = True
file_id = 0
position = 0
for car in line:
	lg = int(car)
	if valid_file:
		map.extend([file_id] * lg)
		files.append([position, lg, file_id])
		file_id += 1
	elif lg != 0:
		map.extend([-1] * lg)
		free_space.append([position, lg])
	position += lg
	valid_file = not valid_file


print_map()

free_idx = 0
last_idx = len(map) - 1

while True:
	while map[free_idx] != -1 and free_idx < len(map):
		free_idx += 1
	while map[last_idx] == -1 and last_idx >= 0:
		last_idx -= 1
	if last_idx < free_idx:
		break
	map[free_idx] = map[last_idx]
	map[last_idx] = -1

print_map()

for idx, l in enumerate(map):
	if l == -1:
		break
	total += idx * l

print(f"Step 1 total {total}")


total = 0
if hasParam("-d"):
	for f in files:
		printD(f"File {f[2]}, position {f[0]} lg: {f[1]}")
	printD("=======")

for r_f_idx, f in enumerate(reversed(files)):
	f_idx = len(files) -1 - r_f_idx
	for idx, space in enumerate(free_space):
		if space[1] >= f[1] and space[0] < f[0]:
			files[f_idx][0] = free_space[idx][0]
			free_space[idx][1] -= files[f_idx][1]
			free_space[idx][0] += files[f_idx][1]
			break

if hasParam("-d"):
	for f in files:
		printD(f"File {f[2]}, position {f[0]} lg: {f[1]}")

print(f"Step 2 total {total}")