#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()

total = 0

def check(result, arguments):
	if len(arguments) == 0:
		return False
	if len(arguments) == 1:
		return result == arguments[0]
	remaining = []
	if len(arguments) > 2:
		remaining = arguments[2:]
	# check with +
	if check(result, [arguments[0] + arguments[1]] + remaining):
		return True
	# check with *
	if check(result, [arguments[0] * arguments[1]] + remaining):
		return True
	# check with ||
	if check(result, [int(f"{arguments[0]}{arguments[1]}")] + remaining):
		return True
	return False

for idx, line in enumerate(lines):
	s = line.split(": ")
	r = int(s[0])
	p = [int(x) for x in s[1].split(" ")]
	if check(r, p):
		total += r

print(f"total: {total}")

