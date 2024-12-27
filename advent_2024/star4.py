#!/usr/bin/python3
from starutils import startTest, printD, toMap, getAt, move, dir8, dir4diag

lines = startTest()
[map, sz] = toMap(lines)

xmas = "XMAS"

total = 0
for y in range(sz[1]):
	for x in range(sz[0]):
		if getAt(map, [x, y], sz) == "X":
			for d in dir8:
				for n in range(1, 4):
					p = move([x, y], d, n)
					if getAt(map, p, sz) != xmas[n]:
						break
					if n == 3:
						printD(f"Found XMAS at {[x,y]} dir {d}")
						total += 1

print(f"Step 1 total: {total}")

total = 0
for y in range(sz[1]):
	for x in range(sz[0]):
		if getAt(map, [x, y], sz) == "A":
			merge = ""
			for d in dir4diag:
				m = getAt(map, move([x, y], d), sz)
				if not m:
					break
				merge += m
			if merge in ["MSSM", "MMSS", "SMMS", "SSMM"]:
				total += 1

print(f"Step 2 total: {total}")
