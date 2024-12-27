#!/usr/bin/python3
from starutils import startTest, printD
import sys

lines = startTest()

total = 0
total_incorrect = 0
o = dict()
o_r = dict()
p = list()
for idx, line in enumerate(lines):
	t = line.split("|")
	if len(t) == 2:
		if int(t[0]) not in o:
			o[int(t[0])] = list()
		o[int(t[0])].append(int(t[1]))
		if int(t[1]) not in o_r:
			o_r[int(t[1])] = list()
		o_r[int(t[1])].append(int(t[0]))
	if len(line.split(",")) > 1:
		p.append([int(x) for x in line.split(",")])

printD("Order:")
printD(o)
printD("\nOrder reverse:")
printD(o_r)
printD("\nPrintings:")
printD(p)
printD("\n")

def validate(pr, o_r):
	valid = True
	for idx, val in enumerate(pr):
		for other in pr[idx+1:]:
			if val in o_r and other in o_r[val]:
				valid = False
				break
		if not valid:
			break
	return valid

for pr in p:
	valid = validate(pr, o_r)
	if valid:
		total += pr[int((len(pr)+1)/2) - 1]
		printD(f"{pr} is valid => ({pr[int((len(pr)+1)/2) - 1]})")
	else:
		pr_sorted = list()
		for val in pr:
			if not len(pr_sorted):
				pr_sorted.append(val)
				continue
			for idx in range(0, len(pr_sorted)+1):
				temp = pr_sorted[:]
				temp.insert(idx, val)
				#print(f"{pr_sorted} => {temp} ({idx})")
				if validate(temp, o_r):
					pr_sorted = temp
					break
		if len(pr_sorted) != len(pr):
			printD(f"compute error {pr} => {pr_sorted}")
			sys.exit(-1)
		total_incorrect += pr_sorted[int((len(pr_sorted)+1)/2) - 1]
		printD(f"{pr} is invalid, sorted is {pr_sorted} => ({pr_sorted[int((len(pr_sorted)+1)/2) - 1]})")

print(f"Step 1 correct:   {total}")
print(f"Step 2 incorrect: {total_incorrect}")
