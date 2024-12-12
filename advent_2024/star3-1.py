#!/usr/bin/python3
import starutils
import re


lines = starutils.startTest()

total = 0
enable = True
for line in lines:
	res = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))", line)
	print(res)
	for item in res:
		if item[2]:
			enable = True
		elif item[3]:
			enable = False
		elif enable:
			total += int(item[0]) * int(item[1])
print(total)
