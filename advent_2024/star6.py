#!/usr/bin/python3
from starutils import startTest, printD, hasParam, toMap, getAt, setAt, move
import copy

total = 0
lines = startTest()
[map, sz] = toMap(lines)

for y in range(sz[1]):
	for x in range(sz[0]):
		v = getAt(map, [x, y], sz)
		if v not in [".", "#"]:
			pos = [x, y]
			if v == "^":
				dir = [0, -1]
			if v == ">":
				dir = [1, 0]
			if v == "v":
				dir = [0, 1]
			if v == "<":
				dir = [-1, 0]
			setAt(map, [x, y], sz, ".")
			printD(f"Found {v} at pos {pos} dir: {dir}")

init_pos = pos[:]
init_dir = dir[:]

if hasParam("-d"):
	for l in map:
		printD("".join(l))

def dir2chr(d):
	if d == [0, -1]:
		return "^"
	if d == [0, 1]:
		return "v"
	if d == [1, 0]:
		return ">"
	if d == [-1, 0]:
		return "<"

if getAt(map, pos, sz) == ".":
	total += 1
	setAt(map, pos, sz, "X")

loop_count = 0
path_items = list()
while True:
	next_pos = move(pos, dir)
	m = getAt(map, next_pos, sz)
	if not m:
		break
	if m == "#":
		# turn right
		next_dir = [-dir[1], dir[0]]
		printD(f"Turn right at pos {pos[0]},{pos[1]} dir: {dir} => {next_dir}")
		dir = next_dir
	else:
		pos = next_pos
		if m == ".":
			total += 1
			path_items.append(next_pos)
			setAt(map, next_pos, sz, "X")

if hasParam("-d"):
	for l in map:
		printD("".join(l))

print(f"Step 1 total: {total}")


def test_path(map, init_pos, dir_init, obstacle):
	pos = init_pos[:]
	dir = dir_init[:]

	while True:
		next_pos = move(pos, dir)
		m = getAt(map, next_pos, sz)
		if not m:
			return False
		if m == "#" or next_pos == obstacle:
			# turn right
			next_dir = [-dir[1], dir[0]]
			printD(f"Turn right at pos {pos[0]},{pos[1]} dir: {dir} => {next_dir}")
			dir = next_dir
		else:
			pos = next_pos
			if getAt(map, next_pos, sz) == dir2chr(dir):
				break
			setAt(map, next_pos, sz, dir2chr(dir))

	printD(f"Loop found in {next_pos[0]}, {next_pos[1]}, with obstacle in {obstacle[0]}, {obstacle[1]}")
	return True

for p in path_items:
	if p == init_pos:
		printD("Skipping init pos")
		continue
	map_copy =copy.deepcopy(map)
	if test_path(map_copy, init_pos, init_dir, p):
		loop_count += 1

print(f"Step 2 Loop count: {loop_count}")


