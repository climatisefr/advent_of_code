#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()
total = 0

line = lines[0]

files = list()
free_space = list()


valid_file = True
file_id = 0
position = 0
for car in line:
	lg = int(car)
	if valid_file:
		files.append([position, lg, file_id])
		file_id += 1
	elif lg != 0:
		free_space.append([position, lg])
	position += lg
	valid_file = not valid_file

for f in files:
	print(f"File {f[2]}, position {f[0]} lg: {f[1]}")
print("=======")

for r_f_idx, f in enumerate(reversed(files)):
	f_idx = len(files) -1 - r_f_idx
	for idx, space in enumerate(free_space):
		if space[1] >= f[1] and space[0] < f[0]:
			files[f_idx][0] = free_space[idx][0]
			free_space[idx][1] -= files[f_idx][1]
			free_space[idx][0] += files[f_idx][1]
			break

string = ['.'] * position

for f in files:
	print(f"File {f[2]}, position {f[0]} lg: {f[1]}")
	for l in range(f[1]):
		total += (f[0] + l) * f[2]
		string[f[0] + l] = str(f[2])


#print("".join(string))

print(f"Total {total}")