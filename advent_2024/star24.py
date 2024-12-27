#!/usr/bin/python3
from starutils import startTest, printD, hasParam
import re

lines = startTest()

items = dict()
init_vals = dict()
swap = [["z09", "gwh"], ["wbw", "wgb"], ["z21", "rcb"], ["z39", "jct"]]

def test_swap(p):
	for s in swap:
		if s[0] == p:
			return s[1]
		if s[1] == p:
			return s[0]
	return p

class item:
	def __init__(self, name, op, left, right):
		self.name = name
		self.std_name = ""
		self.op = op
		self.left = left
		self.right = right
		self.val = -1
		self.str_repr = ""

	def get_val(self, items, init_vals):
		if self.val != -1:
			return self.val
		if self.left in init_vals:
			left = init_vals[self.left]
		else:
			left = items[self.left].get_val(items, init_vals)
		if self.right in init_vals:
			right = init_vals[self.right]
		else:
			right = items[self.right].get_val(items, init_vals)
		if self.op == "OR":
			self.val = left | right
		elif self.op == "XOR":
			self.val = left ^ right
		else:
			self.val = left & right
		return self.val

	def get_repr(self, items, init_vals):
		if self.str_repr != "":
			return self.str_repr
		if self.left in init_vals:
			left = self.left
		else:
			left = items[self.left].get_repr(items, init_vals)
		if self.right in init_vals:
			right = self.right
		else:
			right = items[self.right].get_repr(items, init_vals)
		if right < left:
			tmp = right
			right = left
			left = tmp
		if self.op == "OR":
			self.str_repr = "(" + left + " | " + right + ")"
		elif self.op == "XOR":
			self.str_repr = "(" + left + " ^ " + right + ")"
		else:
			self.str_repr = "(" + left + " & " + right + ")"
		return self.str_repr

	def __repr__(self):
		return f"Item {self.name}: {self.left} {self.op} {self.right}"

items.clear()
init_vals.clear()
for idx, line in enumerate(lines):
	m = re.match(r"([a-z0-9]{3}): ([01])", line)
	if m:
		init_vals[m.group(1)] = int(m.group(2))
	else:
		m = re.match(r"([a-z0-9]{3}) (OR|XOR|AND) ([a-z0-9]{3}) -> ([a-z0-9]{3})", line)
		if m:
			items[test_swap(m.group(4))] = item(test_swap(m.group(4)), m.group(2), m.group(1), m.group(3))
		elif line != "":
			print(f"Unparsed line: {line}")

if hasParam("-d"):
	keys = list(items.keys())
	keys.sort()
	for key in keys:
		printD(f"{key} => {items[key]}")

count = 0
total = 0
keys = list(items.keys())
keys.sort()
for key in keys:
	if key.startswith("z"):
		val = items[key].get_val(items, init_vals)
		total += (val << count)
		count += 1
		if hasParam("-d"):
			rep = items[key].get_repr(items, init_vals)
			printD(f"{key} = {val} = {rep}")

print(f"Step 1 total: {total}")

gen_items = dict()
for i in range(45):
	if i > 0:
		gen_items[f"XOR:{i:02}"] = item(f"XOR:{i:02}", "XOR", f"x{i:02}", f"y{i:02}")
		gen_items[f"AND:{i-1:02}"] = item(f"AND:{i-1:02}", "AND", f"x{i-1:02}", f"y{i-1:02}")
		if i > 1:
			if i > 2:
				gen_items[f"OTH:{i-1:02}"] = item(f"OTH:{i-1:02}", "AND", f"XOR:{i-1:02}", f"RET:{i-2:02}")
			else:
				gen_items[f"OTH:{i-1:02}"] = item(f"OTH:{i-1:02}", "AND", f"XOR:{i-1:02}", f"AND:{i-2:02}")
			gen_items[f"RET:{i-1:02}"] = item(f"RET:{i-1:02}", "OR", f"AND:{i-1:02}", f"OTH:{i-1:02}")
			gen_items[f"z{i:02}"] = item(f"z{i:02}", "XOR", f"XOR:{i:02}", f"RET:{i-1:02}")
		else:
			gen_items[f"z{i:02}"] = item(f"z{i:02}", "XOR", f"XOR:{i:02}", f"AND:{i-1:02}")
	else:
		gen_items[f"z{i:02}"] = item(f"XOR:{i:02}", "XOR", f"x{i:02}", f"y{i:02}")


def compare(str_1, items_1, str_2, items_2):
	if str_1 not in items_1 and str_2 not in items_2:
		if str_1 != str_2:
			return [f"Invalid end points: {str_1} {str_2}"]
		return []
	if str_1 not in items_1:
		return [f"Unexpected END on items_1 {str_1}"]
	if str_2 not in items_2:
		return [f"Unexpected END on items_2 {str_2}"]

	if items_1[str_1].op != items_2[str_2].op:
		return[f"OP Error checking {str_1} and {str_2} ({items_1[str_1].op} != {items_2[str_2].op})"]
	cmp1_L = compare(items_1[str_1].left, items_1, items_2[str_2].left, items_2)
	cmp1_R = compare(items_1[str_1].right, items_1, items_2[str_2].right, items_2)
	#print(f"str_1 {str_1}/str_2 {str_2}: cmp1_L: {cmp1_L}, cmp1_R: {cmp1_R}")
	if len(cmp1_L) == 0 and len(cmp1_R) == 0:
		return []

	cmp2_L = compare(items_1[str_1].left, items_1, items_2[str_2].right, items_2)
	cmp2_R = compare(items_1[str_1].right, items_1, items_2[str_2].left, items_2)
	#print(f"str_1 {str_1}/str_2 {str_2}: cmp2_L: {cmp2_L}, cmp2_R: {cmp2_R}")
	if len(cmp2_L) == 0 and len(cmp2_R) == 0:
		return []
	#print(f"Error detected at {str_1} / {str_2}")
	if len(cmp1_L) + len(cmp1_R) < len(cmp2_L) + len(cmp2_R):
		return cmp1_L + cmp1_R
	else:
		return cmp2_L + cmp2_R

for i in range(45):
	printD(f"Check z{i:02}")
	printD(items[f"z{i:02}"].get_repr(items, init_vals))
	printD(gen_items[f"z{i:02}"].get_repr(gen_items, init_vals))
	res = compare(f"z{i:02}", items, f"z{i:02}", gen_items)
	if res:
		print("* " + "\n* ".join(res))



lst = list()
for s in swap:
	lst.append(s[0])
	lst.append(s[1])
lst.sort()
print("Step 2 swap list: " + ",".join(lst))