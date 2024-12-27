#!/usr/bin/python3
from starutils import startTest, printD, hasParam, getAt, setAt, move, toMap, dir4

lines = startTest()

[map, sz] = toMap(lines)

regions_names = list()

for line in map:
	for x in line:
		if x not in regions_names:
			regions_names.append(x)

if hasParam("-d"):
	for l in map:
		printD("".join(l))


def extract_name(map, name):
	result = list()
	for l in map:
		result.append([name if x == name else "." for x in l])
	return result

def measure_region(map, x, y):
	pos = [x, y]
	val = getAt(map, pos, sz)
	next_pos = list()
	perimeter = 0
	area = 0
	next_pos.append(pos)
	corners = 0
	while next_pos:
		p = next_pos.pop()
		if getAt(map, p, sz) == val:
			area += 1
		else:
			continue
		setAt(map, p , sz, '+')
		for dir in dir4:
			test_pos = move(p, dir)
			test_val = getAt(map, test_pos, sz)
			if test_val == val:
				next_pos.append(test_pos)
			elif test_val != '+':
				perimeter += 1
		for dir in [[[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1], [-1, 0]], [[-1, 0], [0, 1]]]:
			m1 = getAt(map, move(p, dir[0]), sz)
			m2 = getAt(map, move(p, dir[1]), sz)
			m_mid = getAt(map, move(move(p, dir[0]), dir[1]), sz)
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
		printD(f"pos: {p} cur_perimeter: {perimeter}, cur_area {area}, cur_corners {corners}")
	return (perimeter, area, corners)


def find_one_regions(sub_map, name):
	total = 0
	total2 = 0
	for y, l in enumerate(sub_map):
		for x, v in enumerate(l):
			if v == name:
				(perimeter, area, sides) = measure_region(sub_map, x, y)
				printD(f"Start region of {name} in {x},{y} => area: {area}, perimeter: {perimeter}, sides: {sides} => {perimeter * area} / {sides * area}")
				total += perimeter * area
				total2 += sides * area
	return (total, total2)

total = 0
total2 = 0
for name in regions_names:
	sub_map = extract_name(map, name)
	if hasParam("-d"):
		printD(f"Name {name}")
		for l in sub_map:
			printD("".join(l))
	(t, t2) = find_one_regions(sub_map, name)
	total += t
	total2 += t2

print(f"Step 1 total: {total}")
print(f"Step 2 total: {total2}")
