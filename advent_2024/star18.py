#!/usr/bin/python3
from starutils import startTest, printD, getAt, setAt, move, dir4, initMap
import re

lines = startTest()
size = 71

sz = [size, size]
map = initMap(sz, ".")
start = [0, 0]
end = [size -1, size - 1]

obstacles = list()

for idx,line in enumerate(lines):
	m = re.match("(\d+),(\d+)", line)
	if m:
		pt = [int(m.group(1)), int(m.group(2))]
		obstacles.append(pt)

def compute_path():
	full_path = list()
	next_pos = [[start, 0, [start]]]
	min_map = initMap(sz, 10000)
	while next_pos:
		next_pos.sort(key=lambda x: x[1])
		p = next_pos.pop(0)
		#print(f"p: {p}")
		for d in dir4:
			n = move(p[0], d)
			v = getAt(map, n, sz)
			if not v:
				continue
			if v == "#":
				continue
			if getAt(min_map, n, sz) <= p[1] + 1:
				continue
			setAt(min_map, n, sz, p[1] + 1)
			next_pos.append([n, p[1] + 1, p[2] + [n]])
			if n == end:
				printD(f"Reached end with {p[1] + 1} steps")
				next_pos.clear()
				#print(f"p: {p}")
				full_path = p[2] + [n]
				break
	return full_path

for i in range(1024):
	pt = obstacles[i]
	setAt(map, pt, sz, "#")

path = compute_path()
printD(f"Initial path {len(path)}")
print(f"Step 1 steps: {len(path) - 1}")

for j in range(1024, len(obstacles)):
	pt = obstacles[j]
	setAt(map, pt, sz, "#")
	if pt in path:
		new_path = compute_path()
		printD(f"pt {pt} => new_path {len(new_path)}")
		if not new_path:
			print(f"Step 2 position: {pt}")
			break
		path = new_path
