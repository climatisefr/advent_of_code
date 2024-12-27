#!/usr/bin/python3
from starutils import startTest, printD
import re
import math

lines = startTest()
total = 0
total2 = 0

def solve(A, B, prize):
	nb_B = (prize[1] - prize[0] / A[0] * A[1])/(B[1]-B[0]/A[0]*A[1])
	nb_A = (prize[0] - nb_B * B[0]) / A[0]

	nb_A = math.floor(nb_A + 0.5)
	nb_B = math.floor(nb_B + 0.5)

	if prize[0] != nb_A * A[0] + nb_B * B[0] or prize[1] != nb_A * A[1] + nb_B * B[1]:
		printD(f" A: {A}, B: {B}, prize: {prize} => No solution")
		return -1

	count = 3 * nb_A + nb_B
	printD(f" A: {A}, B: {B}, prize: {prize} => nb_A: {nb_A}, nb_B: {nb_B} => {prize[1]} ?= {A[1] * nb_A + B[1] * nb_B} => count {count}")
	return count


for idx,line in enumerate(lines):
	m = re.match("Button A: X\+(\d+), Y\+(\d+)", line)
	if m:
		A = [int(m.group(1)), int(m.group(2))]
	m = re.match("Button B: X\+(\d+), Y\+(\d+)", line)
	if m:
		B = [int(m.group(1)), int(m.group(2))]
	m = re.match("Prize: X=(\d+), Y=(\d+)", line)
	if m:
		prize = [int(m.group(1)), int(m.group(2))]
		v = solve(A, B, prize)
		if v >= 0:
			total += v
		prize = [10000000000000 + prize[0], 10000000000000 + prize[1]]
		v = solve(A, B, prize)
		if v >= 0:
			total2 += v

print(f"Step 1 total: {total}")
print(f"Step 2 total: {total2}")
