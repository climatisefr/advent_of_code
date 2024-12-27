#!/usr/bin/python3
from starutils import startTest, printD, toMap, getAt, hasParam, setAt, move
import copy

lines = startTest()
[map, sz] = toMap(lines)
map2 = copy.deepcopy(map)
total = 0


antenas = dict()

for y in range(sz[1]):
	for x in range(sz[0]):
		v = getAt(map, [x, y], sz)
		if v == ".":
			continue
		if v not in antenas:
			antenas[v] = list()
		antenas[v].append([x, y])
printD(f"antenas {antenas}")

for key, v in antenas.items():
	printD(f"key {key}, v {v}")
	for idx, item1 in enumerate(v):
		for item2 in v[idx+1:]:
			delta = [item2[0] - item1[0], item2[1] - item1[1]]
			setAt(map, move(item2, delta), sz, "#")
			setAt(map, move(item1, delta, -1), sz, "#")

			mult = 0
			while True:
				pos = move(item2, delta, mult)
				if not getAt(map, pos, sz):
					break
				setAt(map2, pos, sz, "#")
				mult += 1

			mult = 0
			while True:
				pos = move(item1, delta, -mult)
				if not getAt(map, pos, sz):
					break
				setAt(map2, pos, sz, "#")
				mult += 1

if hasParam("-d"):
	for l in map:
		printD("".join(l))

total = 0
for l in map:
	for p in l:
		if p == "#":
			total += 1
print(f"Step 1 total: {total}")

total = 0
for l in map2:
	for p in l:
		if p == "#":
			total += 1
print(f"Step 2 total: {total}")

