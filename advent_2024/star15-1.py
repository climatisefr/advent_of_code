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
			robots.append([line.find("@"), idx])
			line = line.replace("@", ".")
		map.append([x for x in line])
	m = re.match("([<>^v]+)", line)
	if m:
		char2dir = {"v": [0, 1], "<": [-1, 0], "^": [0, -1], ">": [1, 0]}
		moves.extend([char2dir[x] for x in line])

for l in map:
	print("".join(l))
print(f"\nMoves: {moves}")
print(f"Robots: {robots}")

def push(p, d):
	next = [p[0] + d[0], p[1] + d[1]]
	if map[next[1]][next[0]] == ".":
		# move is OK not more action
		return next
	if map[next[1]][next[0]] == "O":
		# need to move box
		box_pos = push(next, d)
		if box_pos != next:
			# box moved
			map[next[1]][next[0]] = "."
			map[box_pos[1]][box_pos[0]] = "O"
			return next
		return p
	if map[next[1]][next[0]] == "#":
		return p


robot = robots[0]
for move in moves:
	next = push(robot, move)
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
		if i == "O":
			total += 100 * y + x

print(f"Total {total}")
