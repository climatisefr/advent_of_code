#!/usr/bin/python3
import starutils
import re
import sys
import copy
import math

lines = starutils.startTest()
robots = list()
total = 0

w = 101
h = 103

for idx,line in enumerate(lines):
	m = re.match("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
	if m:
		robots.append([[int(m.group(1)), int(m.group(2))], [int(m.group(3)), int(m.group(4))]])
	else:
		print(f"Unmatched line {line}")

for idx, r in enumerate(robots):
	pos = r[0]
	vel = r[1]
	cur_pos = [(pos[0] + vel[0]) % w, (pos[1] + vel[1]) % h]
	count = 1
	while cur_pos != pos:
		cur_pos = [(cur_pos[0] + vel[0]) % w, (cur_pos[1] + vel[1]) % h]
		#print(f"{cur_pos}")
		count += 1
	#print(f"{idx}) => {count}")


pos = [r[0] for r in robots]
vel = [r[1] for r in robots]

count = 0
max_consec_global = 0
while count <= 10403:

	for i in range(len(pos)):
		pos[i][0] = (pos[i][0] + vel[i][0]) % w
		pos[i][1] = (pos[i][1] + vel[i][1]) % h
	count += 1

	map = [[" "] * w for _ in range(h)]
	for p in pos:
		map[p[1]][p[0]] = "*"
	found = False
	max_consec = 0
	count_consec = 0
	for l in map:
		for p in l:
			if p == "*":
				count_consec += 1
				if count_consec > max_consec:
					max_consec = count_consec
			else:
				count_consec = 0

	if max_consec > max_consec_global:
		max_consec_global = max_consec
		print(f"Count: {count} {max_consec}")
		for l in map:
			print("".join(l))

