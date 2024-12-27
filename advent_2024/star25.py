#!/usr/bin/python3
from starutils import startTest, printD
import re

lines = startTest()
total = 0

keys = list()
locks = list()

tmp = list()
lines.append("")

for idx, line in enumerate(lines):
	m = re.match(r"([\.#]+)", line)
	if m:
		tmp.append(line)
	elif line == "":
		vals = [0] * 5
		for l in tmp[1:-1]:
			printD(l)
		type = tmp[0][0]
		for n, l in enumerate(tmp[1:-1]):
			for i, v in enumerate(l):
				if v == type:
					vals[i] = n + 1
		printD(f"Type: {type}, vals: {vals}")
		if type == "#":
			locks.append(vals)
		else:
			keys.append([5 - x for x in vals])
		tmp.clear()
	else:
		printD(f"Unmatched line: {line}")


printD("Keys:")
for k in keys:
	printD(k)
printD("Locks:")
for l in locks:
	printD(l)

for l in locks:
	for k in keys:
		valid = True
		for i in range(len(k)):
			if k[i] + l[i] >= 6:
				valid = False
				break
		if valid:
			total += 1

print(f"Step 1 total: {total}")