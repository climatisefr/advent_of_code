#!/usr/bin/python3
from starutils import startTest, printD, hasParam, getAt, setAt, move, toMap, dir4, initMap

lines = startTest()

[map, sz] = toMap(lines)
start = list()
end = list()

dir = [1, 0]

for idx, line in enumerate(map):
	if "S" in line:
		start = [line.index("S"), idx]
		setAt(map, start, sz, ".")
	if "E" in line:
		end = [line.index("E"), idx]
		setAt(map, end, sz, ".")

if hasParam("-d"):
	for l in map:
		printD("".join(l))
	printD(f"Start: {start}, end: {end}")


def compute(cheat_length):
	total = 0
	counts = initMap(sz, -1)
	cheat_pos = list()
	pos = start
	steps = 0
	setAt(counts, start, sz, 0)
	while pos != end:
		steps += 1
		for d in dir4:
			n = move(pos, d)
			v = getAt(map, n, sz)
			printD(f"Test pos {n}: {v}")
			if v == "." and getAt(counts, n, sz) == -1:
				next = n
				setAt(counts, n, sz, steps)
		pos = next
		for x in range(-cheat_length, cheat_length + 1):
			for y in range(-cheat_length, cheat_length + 1):
				lg = (x if x >= 0 else -x) + (y if y >= 0 else -y)
				if lg > cheat_length:
					continue
				n = move(pos, [x, y])
				v = getAt(map, n, sz)
				if not v or getAt(counts, n, sz) == -1:
					continue
				if getAt(counts, pos, sz) - getAt(counts, n, sz) - lg > 0:
					cheat_pos.append([n, pos, getAt(counts, pos, sz) - getAt(counts, n, sz) - lg])

	printD(f"steps: {steps}")

	cheat_pos.sort(key=lambda x: x[2])
	cheat_count = dict()
	total = 0
	for l in cheat_pos:
		cheat_count[l[2]] = cheat_count.get(l[2], 0) + 1
		if l[2] >= 100:
			total += 1

	if hasParam("-d"):
		items = list(cheat_count.keys())
		items.sort()
		for i in items:
			printD(f"{cheat_count[i]} cheats save {i} picoseconds")
	return total

print(f"Step 1 total: {compute(2)}")
print(f"Step 2 total: {compute(20)}")