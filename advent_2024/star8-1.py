#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()

total = 0


antenas = dict()
w = len(lines[0])
h = len(lines)
map = [["." for _ in range(w)] for _ in range(h)]
map_bin = [[0 for _ in range(w)] for _ in range(h)]

for y, line in enumerate(lines):
	for x, v in enumerate(line):
		if v != ".":
			if v not in antenas:
				antenas[v] = list()
			antenas[v].append([x, y])
			map[y][x] = v
print(f"antenas {antenas}")

for key, v in antenas.items():
	print(f"key {key}, v {v}")
	for idx, item1 in enumerate(v):
		for item2 in v[idx+1:]:
			delta = [item2[0] - item1[0], item2[1] - item1[1]]
			mult = 0
			while True:
				pos1 = [item2[0] + mult * delta[0], item2[1] + mult * delta[1]]
				if pos1[0] >= 0 and pos1[0] < w and pos1[1] >= 0 and pos1[1] < h:
					map[pos1[1]][pos1[0]] = "#"
					map_bin[pos1[1]][pos1[0]] = 1
				else:
					break
				mult += 1

			mult = 0
			while True:
				pos2 = [item1[0] - mult * delta[0], item1[1] - mult * delta[1]]
				if pos2[0] >= 0 and pos2[0] < w and pos2[1] >= 0 and pos2[1] < h:
					map[pos2[1]][pos2[0]] = "#"
					map_bin[pos2[1]][pos2[0]] = 1
				else:
					break
				mult += 1

for l in map:
	print("".join(l))
total = 0
for l in map_bin:
	total += sum(l)

print(f"total: {total}")

