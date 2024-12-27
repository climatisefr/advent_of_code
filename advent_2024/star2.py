#!/usr/bin/python3
from starutils import startTest

lines = startTest()

def valid_seq(items):
	last_val = items[0]
	increase = True if items[1] > items[0] else False
	for i in items[1:]:
		if not((increase and (i - last_val) in [1, 2, 3]) or (not increase and (last_val - i) in [1, 2, 3])):
			return False
		else:
			last_val = i
	return True

total_safe_count = 0
total_safe_count_2 = 0
for l in lines:
	items = [int(x) for x in l.split(" ")]
	if valid_seq(items):
		total_safe_count_2 += 1
		total_safe_count += 1
	else:
		for i in range(len(items)):
			sub_items = [value for idx,value in enumerate(items) if idx != i]
			if valid_seq(sub_items):
				total_safe_count_2 += 1
				break

print(f"Step 1 Safe_count {total_safe_count}")
print(f"Step 2 Safe_count {total_safe_count_2}")