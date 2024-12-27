#!/usr/bin/python3
from starutils import startTest, printD, hasParam, move, getAt, setAt
import re

lines = startTest()
total = 0

map = list()
map2 = list()
moves = list()
robot = list()

for idx,line in enumerate(lines):
	m = re.match("([#.O@]+)", line)
	if m:
		if "@" in line:
			robot =[line.find("@"), idx]
			line = line.replace("@", ".")
		map.append([x for x in line])
		line = line.replace("#", "##")
		line = line.replace(".", "..")
		line = line.replace("O", "[]")
		map2.append([x for x in line])
	m = re.match("([<>^v]+)", line)
	if m:
		char2dir = {"v": [0, 1], "<": [-1, 0], "^": [0, -1], ">": [1, 0]}
		moves.extend([char2dir[x] for x in line])

if hasParam("-d"):
	for l in map:
		printD("".join(l))
	printD(f"\nMoves: {moves}")
	printD(f"Robots: {robot}")

def push(map, sz, p, d):
	next = move(p, d)
	if getAt(map, next, sz) == ".":
		# move is OK not more action
		return next
	if getAt(map, next, sz) == "O":
		# need to move box
		box_pos = push(map, sz, next, d)
		if box_pos != next:
			# box moved
			setAt(map, next, sz, ".")
			setAt(map, box_pos, sz, "O")
			return next
		return p
	if getAt(map, next, sz) == "#":
		return p

def test_push(map, sz, p, d):
	next = move(p, d)
	if  getAt(map, next, sz) == ".":
		# move is OK not more action
		return True
	if  getAt(map, next, sz) in ["[", "]"] and d[1] == 0:
		# need to move box
		return test_push(map, sz, next, d)
	if  getAt(map, next, sz) == "[" and d[1] != 0:
		# need to move box
		return test_push(map, sz, next, d) and test_push(map, sz, [next[0]+1, next[1]],d)
	if  getAt(map, next, sz) == "]" and d[1] != 0:
		# need to move box
		return test_push(map, sz, next, d) and test_push(map, sz, [next[0]-1, next[1]],d)
	if  getAt(map, next, sz) == "#":
		return False

def push_verified(map, sz, p, d):
	next = [p[0] + d[0], p[1] + d[1]]
	if  getAt(map, next, sz) == ".":
		# move is OK not more action
		return next
	if  getAt(map, next, sz) in ["[", "]"] and d[1] == 0:
		# need to move box
		item =  getAt(map, next, sz)
		box_pos = push_verified(map, sz, next, d)
		setAt(map, next, sz, ".")
		setAt(map, box_pos, sz, item)
		return next
	if  getAt(map, next, sz) == "[" and d[1] != 0:
		# need to move box
		box_pos = push_verified(map, sz, next, d)
		setAt(map, next, sz, ".")
		setAt(map, box_pos, sz, "[")
		box_pos = push_verified(map, sz, [next[0] + 1, next[1]], d)
		setAt(map, move(next, [1, 0]), sz, ".")
		setAt(map, box_pos, sz, "]")
		return next
	if  getAt(map, next, sz) == "]" and d[1] != 0:
		# need to move box
		box_pos = push_verified(map, sz, next, d)
		setAt(map, next, sz, ".")
		setAt(map, box_pos, sz, "]")
		box_pos = push_verified(map, sz, [next[0] - 1, next[1]], d)
		setAt(map, move(next, [-1, 0]), sz, ".")
		setAt(map, box_pos, sz, "[")
		return next
	if  getAt(map, next, sz) == "#":
		return p

r = robot
for m in moves:
	next = push(map, [len(map[0]), len(map)], r, m)
	printD(f"Robot {r} => {next} [move {m}]")
	r = next

for y, l in enumerate(map):
	for x, i in enumerate(l):
		if i == "O":
			total += 100 * y + x

print(f"Step 1 total: {total}")

total = 0
r = robot
# for step 2 multiply x of robot by 2
r[0] *= 2
for m in moves:
	if test_push(map2, [len(map2[0]), len(map2)], r, m):
		next = push_verified(map2, [len(map2[0]), len(map2)], r, m)
	else:
		next = r
	printD(f"Robot {r} => {next} [move {m}]")
	r = next

for y, l in enumerate(map2):
	for x, i in enumerate(l):
		if i == "[":
			total += 100 * y + x

print(f"Step 2 total: {total}")
