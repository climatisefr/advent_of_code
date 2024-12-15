#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()
total = 0

map = list()

regions_names = list()

for idx,line in enumerate(lines):
	map.append([x for x in line])
	for x in line:
		if x not in regions_names:
			regions_names.append(x)

#for l in map:
#	print("".join(l))


def extract_name(map, name):
	result = list()
	for l in map:
		result.append([name if x == name else "." for x in l])
	return result

def map_val(map, x, y):
	if x >= 0 and y >= 0 and x < len(map[0]) and y < len(map):
		return map[y][x]
	return "°"


def measure_region(map, x, y):
	val = map[y][x]
	pos = [x, y]
	next_pos = list()
	perimeter = 0
	area = 0
	next_pos.append(pos)
	corners = 0
	while next_pos:
		p = next_pos.pop()
		if map[p[1]][p[0]] == val:
			area += 1
		else:
			continue
		map[p[1]][p[0]] = '+'
		for dir in [[0,1], [1, 0], [0, -1], [-1, 0]]:
			test_pos = [p[0] + dir[0], p[1] + dir[1]]
			test_val = map_val(map,test_pos[0], test_pos[1])
			if test_val == val:
				next_pos.append(test_pos)
			elif test_val != '+':
				perimeter += 1
		for dir in [[[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]], [[-1, 0], [0, 1]]]:
			m1 = map_val(map, p[0] + dir[0][0], p[1] + dir[0][1])
			m2 = map_val(map, p[0] + dir[1][0], p[1] + dir[1][1])
			m_mid = map_val(map, p[0] + dir[0][0] + dir[1][0], p[1] + dir[0][1] + dir[1][1])
			if m1 == "+":
				m1 = val
			if m2 == "+":
				m2 = val
			if m_mid == "+":
				m_mid = val
			if m1 != val and m2 != val:
				corners += 1
			if m1 == val and m2 == val and m_mid != val:
				corners += 1
		#print(f"pos: {p} cur_perimeter: {perimeter}, cur_area {area}, cur_corners {corners}")

	return (perimeter, area, corners)


def find_one_regions(sub_map, name):
	total = 0
	total2 = 0
	for y, l in enumerate(sub_map):
		for x, v in enumerate(l):
			if v == name:
				(perimeter, area, sides) = measure_region(sub_map, x, y)
				print(f"Start region of {name} in {x},{y} => area: {area}, perimeter: {perimeter}, sides: {sides} => {perimeter * area} / {sides * area}")
				total += perimeter * area
				total2 += sides * area
	return (total, total2)

total2 = 0
for name in regions_names:
	sub_map = extract_name(map, name)
	#print(f"Name {name}")
	#for l in sub_map:
	#	print("".join(l))
	(t, t2) = find_one_regions(sub_map, name)
	total += t
	total2 += t2


print(f"Total {total}")
print(f"Total2 {total2}")
