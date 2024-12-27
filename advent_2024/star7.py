#!/usr/bin/python3
from starutils import startTest


lines = startTest()

def check(result, arguments, v2):
	if len(arguments) == 0:
		return False
	if len(arguments) == 1:
		return result == arguments[0]
	remaining = []
	if len(arguments) > 2:
		remaining = arguments[2:]
	# check with +
	if check(result, [arguments[0] + arguments[1]] + remaining, v2):
		return True
	# check with *
	if check(result, [arguments[0] * arguments[1]] + remaining, v2):
		return True
	if v2:
		# check with ||
		if check(result, [int(f"{arguments[0]}{arguments[1]}")] + remaining, v2):
			return True
	return False

total = 0
for line in lines:
	s = line.split(": ")
	r = int(s[0])
	p = [int(x) for x in s[1].split(" ")]
	if check(r, p, False):
		total += r

print(f"Step 1 total: {total}")

total = 0
for line in lines:
	s = line.split(": ")
	r = int(s[0])
	p = [int(x) for x in s[1].split(" ")]
	if check(r, p, True):
		total += r

print(f"Step 2 total: {total}")

