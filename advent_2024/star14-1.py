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

print(f"{robots}")

def calc_pos(robot, time, w, h):
	p = robot[0]
	v = robot[1]
	p = [(p[0] + time * v[0]) % w, (p[1] + time * v[1])%h]
	return p

quadrant = [0] * 4
for idx, robot in enumerate(robots):
	p = calc_pos(robot, 100, w, h)
	print(f"{idx}) {robot[0]} ({robot[1]}) => {p}")
	if p[0] < int((w-1)/2) and p[1] < int((h-1)/2):
		quadrant[0] += 1
	if p[0] < int((w-1)/2) and p[1] > int((h-1)/2):
		quadrant[1] += 1
	if p[0] > int((w-1)/2) and p[1] < int((h-1)/2):
		quadrant[2] += 1
	if p[0] > int((w-1)/2) and p[1] > int((h-1)/2):
		quadrant[3] += 1

print(f"Quadrants: {quadrant}")
total = 1
for q in quadrant:
	total *= q
print(f"Total {total}")
