#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()
total = 0

map = list()
heads = list()

for idx, line in enumerate(lines):
	map.append([int(x) for x in line])
	h = [[x, idx] for x,v in enumerate(line) if v == "0"]
	heads.extend(h)
print(heads)

def find_next(pos):
	next_pos = list()
	cur_val = map[pos[1]][pos[0]]
	for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
		n = [pos[0] + dir[0], pos[1] + dir[1]]
		if n[0] >= 0 and n[0] < len(map[0]) and n[1] >= 0 and n[1] < len(map):
			if cur_val + 1 == map[n[1]][n[0]]:
				next_pos.append(n)
	#print(f"p {pos}:{cur_val} => {next_pos}")
	return next_pos


def find_path(src, positions):
	ret_val = dict()
	for p in positions:
		#print(f"pos {p}")
		if map[p[1]][p[0]] == 9:
			#print(f"Reach 9 in {p}")
			ident = str(src) + " => " + str(p)
			ret_val[ident] = ret_val.get(ident, 0) + 1
		else:
			n = find_next(p)
			ret = find_path(src, n)
			for r,v in ret.items():
				ret_val[r] = ret_val.get(r, 0) + v
	#print(f"ret_val {ret_val}")
	return ret_val

total2 = 0
for src in heads:
	f = find_path(src, [src])
	sub_total = sum([f[x] for x in f])
	print(f"{src} => {len(f)} / {sub_total}")
	total += len(f)
	total2 += sub_total

print(f"Total {total}")
print(f"Total2: {total2}")