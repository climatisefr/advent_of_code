#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()
total = 0

stones = [int(x) for x in lines[0].split(' ')]

print(f"{stones}")

def blink(input):
	output = list()
	for s in input:
		if s == 0:
			output.append(1)
		elif len(str(s)) & 1 == 0:
			lg = len(str(s))
			left = str(s)[:int(lg/2)]
			right = str(s)[int(lg/2):]
			output.append(int(left))
			output.append(int(right))
		else:
			output.append(s*2024)
	return output

for i in range(75):
	stones = blink(stones)
	#print(f"({i+1}) [{len(stones)}] {stones}")
	print(f"({i+1}) [{len(stones)}]")

#print(f"Total {total}")
