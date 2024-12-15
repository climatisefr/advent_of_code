#!/usr/bin/python3
import starutils
import re
import sys
import copy
import math

lines = starutils.startTest()
total = 0

map = list()
moves = list()
robots = list()

for idx,line in enumerate(lines):
	m = re.match("([#.O@]+)", line)
	if m:
		if "@" in line:
			robots.append([2 * line.find("@"), idx])
			line = line.replace("@", ".")
		line = line.replace("#", "##")
		line = line.replace(".", "..")
		line = line.replace("O", "[]")
		map.append([x for x in line])
	m = re.match("([<>^v]+)", line)
	if m:
		char2dir = {"v": [0, 1], "<": [-1, 0], "^": [0, -1], ">": [1, 0]}
		moves.extend([char2dir[x] for x in line])

for l in map:
	print("".join(l))
print(f"\nMoves: {moves}")
print(f"Robots: {robots}")

def test_push(p, d):
	next = [p[0] + d[0], p[1] + d[1]]
	if map[next[1]][next[0]] == ".":
		# move is OK not more action
		return True
	if map[next[1]][next[0]] in ["[", "]"] and d[1] == 0:
		# need to move box
		return test_push(next, d)
	if map[next[1]][next[0]] == "[" and d[1] != 0:
		# need to move box
		return test_push(next, d) and test_push([next[0]+1, next[1]],d)
	if map[next[1]][next[0]] == "]" and d[1] != 0:
		# need to move box
		return test_push(next, d) and test_push([next[0]-1, next[1]],d)
	if map[next[1]][next[0]] == "#":
		return False

def push_verified(p, d):
	next = [p[0] + d[0], p[1] + d[1]]
	if map[next[1]][next[0]] == ".":
		# move is OK not more action
		return next
	if map[next[1]][next[0]] in ["[", "]"] and d[1] == 0:
		# need to move box
		item = map[next[1]][next[0]]
		box_pos = push_verified(next, d)
		map[next[1]][next[0]] = "."
		map[box_pos[1]][box_pos[0]] = item
		return next
	if map[next[1]][next[0]] == "[" and d[1] != 0:
		# need to move box
		box_pos = push_verified(next, d)
		map[next[1]][next[0]] = "."
		map[box_pos[1]][box_pos[0]] = "["
		box_pos = push_verified([next[0] + 1, next[1]], d)
		map[next[1]][next[0] + 1] = "."
		map[box_pos[1]][box_pos[0]] = "]"
		return next
	if map[next[1]][next[0]] == "]" and d[1] != 0:
		# need to move box
		box_pos = push_verified(next, d)
		map[next[1]][next[0]] = "."
		map[box_pos[1]][box_pos[0]] = "]"
		box_pos = push_verified([next[0] - 1, next[1]], d)
		map[next[1]][next[0] - 1] = "."
		map[box_pos[1]][box_pos[0]] = "["
		return next
	if map[next[1]][next[0]] == "#":
		return p


robot = robots[0]
for move in moves:
	if test_push(robot, move):
		next = push_verified(robot, move)
	else:
		next = robot
	print(f"Robot {robot} => {next} [move {move}]")
	robot = next
	#for idx, l in enumerate(map):
	#	if robot[1] == idx:
	#		tmp = l[:]
	#		tmp[robot[0]] = "@"
	#		print("".join(tmp))
	#	else:
	#		print("".join(l))

for y, l in enumerate(map):
	for x, i in enumerate(l):
		if i == "[":
			total += 100 * y + x

print(f"Total {total}")
