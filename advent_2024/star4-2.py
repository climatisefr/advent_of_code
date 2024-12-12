#!/usr/bin/python3
import starutils
import re


lines = starutils.startTest()

xmas = "MAS"

total = 0
for idx, line in enumerate(lines):
	for pos in range(0, len(line)):
		if line[pos] == 'A' and idx + 1 < len(lines) and idx - 1 >= 0 and pos + 1 < len(line) and pos - 1 >= 0:
			a = lines[idx - 1][pos - 1]
			b = lines[idx - 1][pos + 1]
			c = lines[idx + 1][pos - 1]
			d = lines[idx + 1][pos + 1]
			tot = a + b + c + d
			if tot == 'MSMS' or tot == "MMSS" or tot == "SMSM" or tot == "SSMM":
				total += 1

print(total)
