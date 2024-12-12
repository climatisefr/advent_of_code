#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()

total = 0
map = list()
pos = [0, 0]
dir = [0, 0]
for idx, line in enumerate(lines):
	remain = line.replace(".", "").replace("#", "")
	if remain:
		pos[0] = line.find(remain)
		pos[1] = idx
		if remain == "^":
			dir = [0, -1]
		if remain == ">":
			dir = [1, 0]
		if remain == "v":
			dir = [0, 1]
		if remain == "<":
			dir = [-1, 0]
		print(f"Found {remain} at pos {pos[0]},{pos[1]} dir: {dir}")
		line = line.replace(remain, ".")
	map.append([x for x in line])

init_pos = pos[:]
init_dir = dir[:]

#for l in map:
#	print("".join(l))

if map[pos[1]][pos[0]] == ".":
	total += 1
#map[pos[1]][pos[0]] = "X"
if dir == [0, -1]:
	map[pos[1]][pos[0]] = "^"
if dir == [0, 1]:
	map[pos[1]][pos[0]] = "v"
if dir == [1, 0]:
	map[pos[1]][pos[0]] = ">"
if dir == [-1, 0]:
	map[pos[1]][pos[0]] = "<"

def dir_to_idx(_dir):
	if dir == [0, -1]:
		return 0
	if dir == [1, 0]:
		return 1
	if dir == [0, 1]:
		return 2
	if dir == [-1, 0]:
		return 3

def move_dir(pos, dir):
	return [pos[0] + dir[0], pos[1] + dir[1]]


loop_count = 0
path_items = list()
while True:
	next_pos = move_dir(pos, dir)
	if not (next_pos[0] >= 0 and next_pos[0] < len(lines[0]) and next_pos[1] >= 0 and next_pos[1] < len(lines)):
		break
	if map[next_pos[1]][next_pos[0]] == "#":
		next_dir = [-dir[1], dir[0]]
		#print(f"Turn right at pos {pos[0]},{pos[1]} dir: {dir} => {next_dir}")
		dir = next_dir
	else:
		pos = next_pos
		if map[next_pos[1]][next_pos[0]] == ".":
			total += 1
			path_items.append(next_pos)
		map[next_pos[1]][next_pos[0]] = "X"

print(f"total: {total}")


def test_path(map, init_pos, dir_init, obstacle):
	pos = init_pos[:]
	dir = dir_init[:]

	while True:
		next_pos = move_dir(pos, dir)
		if not (next_pos[0] >= 0 and next_pos[0] < len(map[0]) and next_pos[1] >= 0 and next_pos[1] < len(map)):
			return False
		if map[next_pos[1]][next_pos[0]] == "#" or next_pos == obstacle:
			next_dir = [-dir[1], dir[0]]
			#print(f"Turn right at pos {pos[0]},{pos[1]} dir: {dir} => {next_dir}")
			dir = next_dir
		else:
			pos = next_pos

			if dir == [0, -1]:
				if map[next_pos[1]][next_pos[0]] == "^":
					break
				map[next_pos[1]][next_pos[0]] = "^"
			if dir == [0, 1]:
				if map[next_pos[1]][next_pos[0]] == "v":
					break
				map[next_pos[1]][next_pos[0]] = "v"
			if dir == [1, 0]:
				if map[next_pos[1]][next_pos[0]] == ">":
					break
				map[next_pos[1]][next_pos[0]] = ">"
			if dir == [-1, 0]:
				if map[next_pos[1]][next_pos[0]] == "<":
					break
				map[next_pos[1]][next_pos[0]] = "<"

	#print(f"Loop found in {next_pos[0]}, {next_pos[1]}, with obstacle in {obstacle[0]}, {obstacle[1]}")

	return True


#for l in map:
#	print("".join(l))

for p in path_items:
	if p == init_pos:
		print("Skipping init pos")
		continue
	map_copy =copy.deepcopy(map)
	if test_path(map_copy, init_pos, init_dir, p):
		loop_count += 1

print(f"Loop count: {loop_count}")


