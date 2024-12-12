#!/usr/bin/python3
import starutils
import re
import sys
import copy

lines = starutils.startTest()
total = 0

total_count = 74

stones = [[int(x), total_count] for x in lines[0].split(' ')]

print(f"{stones}")

storage = dict()

def blink(s):
	output = list()
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

for i in range(total_count):
	next = list()
	for stone in stones:
		[s,c] = stone
		if s not in storage:
			n = blink(s)
			storage[s] = list()
			next.extend([v, total_count - i] for v in n)
		else:
			next.append([s, c])
	stones = next
	print(f"({i+1}) [{len(stones)}] {stones}")
print(f"storage: {len(storage)}")

def calc(s):
	#print(f"calc({s})")
	if s[0] not in storage:
		storage[s[0]] = list()
	if len(storage[s[0]]) > s[1] and storage[s[0]][s[1]] != 0:
		return storage[s[0]][s[1]]
	if len(storage[s[0]]) <= s[1]:
		storage[s[0]].extend([0] * (s[1] - len(storage[s[0]]) + 1))
	if s[1] == 0:
		storage[s[0]][0] = 1
		return 1
	n = blink(s[0])
	for item in n:
		storage[s[0]][s[1]] += calc([item, s[1]-1])
	return storage[s[0]][s[1]]

for s in stones:
	t = calc(s)
	total += t
	print(f"{s} -> {t}")

print(f"Total {total}")
