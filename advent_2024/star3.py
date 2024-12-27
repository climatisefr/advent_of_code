#!/usr/bin/python3
from starutils import startTest, printD
import re

lines = startTest()

total = 0
total2 = 0
enable = True
for line in lines:
	res = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))", line)
	printD(res)
	for item in res:
		if item[2]:
			enable = True
		elif item[3]:
			enable = False
		elif enable:
			total2 += int(item[0]) * int(item[1])
			total += int(item[0]) * int(item[1])
		else:
			total += int(item[0]) * int(item[1])

print(f"Step 1 total: {total}")
print(f"Step 2 total: {total2}")
