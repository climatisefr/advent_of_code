#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()
total = 0

line = lines[0]

map = list()

def print_map():
	str_result = ""
	for l in map:
		if l == -1:
			str_result += "."
		else:
			str_result += str(l)
	print(str_result)


valid_file = True
file_id = 0

for car in line:
	lg = int(car)
	if valid_file:
		map.extend([file_id] * lg)
		file_id += 1
	elif lg != 0:
		map.extend([-1] * lg)
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

print(f"Total {total}")