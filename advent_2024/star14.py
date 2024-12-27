#!/usr/bin/python3
from starutils import startTest, printD, setAt, hasParam, initMap
import re

lines = startTest()
robots = list()

w = 101
h = 103

for idx,line in enumerate(lines):
	m = re.match("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
	if m:
		robots.append([[int(m.group(1)), int(m.group(2))], [int(m.group(3)), int(m.group(4))]])
	else:
		printD(f"Unmatched line {line}")

printD(f"{robots}")

def calc_pos(robot, time, w, h):
	p = robot[0]
	v = robot[1]
	p = [(p[0] + time * v[0]) % w, (p[1] + time * v[1])%h]
	return p

quadrant = [0] * 4
for idx, robot in enumerate(robots):
	p = calc_pos(robot, 100, w, h)
	printD(f"{idx}) {robot[0]} ({robot[1]}) => {p}")
	if p[0] < int((w-1)/2) and p[1] < int((h-1)/2):
		quadrant[0] += 1
	if p[0] < int((w-1)/2) and p[1] > int((h-1)/2):
		quadrant[1] += 1
	if p[0] > int((w-1)/2) and p[1] < int((h-1)/2):
		quadrant[2] += 1
	if p[0] > int((w-1)/2) and p[1] > int((h-1)/2):
		quadrant[3] += 1

printD(f"Quadrants: {quadrant}")
total = 1
for q in quadrant:
	total *= q
print(f"Step 1 total: {total}")

pos = [r[0] for r in robots]
vel = [r[1] for r in robots]

count = 0
max_consec_global = 0
max_consec_count = 0
while count <= w * h:

	for i in range(len(pos)):
		pos[i][0] = (pos[i][0] + vel[i][0]) % w
		pos[i][1] = (pos[i][1] + vel[i][1]) % h
	count += 1

	map = initMap([w, h], " ")
	for p in pos:
		setAt(map, p , [w, h], "*")
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
		max_consec_count = count
		if hasParam("-d"):
			printD(f"Count: {count} {max_consec}")
			for l in map:
				printD("".join(l))

print(f"Step 2 count: {max_consec_count}")
