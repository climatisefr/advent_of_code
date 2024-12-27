#!/usr/bin/python3
from starutils import startTest, printD
from functools import cache

lines = startTest()

keypad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['', '0', 'A']]
keys = '0123456789A'
arrows = '<v>^A'
keypad_arrows = [['', '^', 'A'], ['<', 'v', '>']]
keypad_distances = dict()
keypad_arrow_distances = dict()

def find_pos(pads, key):
	for y, l in enumerate(pads):
		for x, k in enumerate(l):
			if k == key:
				return [x, y]

def calc_moves(p1, p2, exclude_pos):
	h = ""
	if p2[0] < p1[0]:
		h = "<" * (p1[0] - p2[0])
	if p2[0] > p1[0]:
		h = ">" * (p2[0] - p1[0])
	v = ""
	if p2[1] < p1[1]:
		v = "^" * (p1[1] - p2[1])
	if p2[1] > p1[1]:
		v = "v" * (p2[1] - p1[1])
	if h == "":
		return [v]
	elif v == "":
		return [h]
	else:
		# exclude path over ''
		if p1[0] == exclude_pos[0] and p2[1] == exclude_pos[1]:
			return [h + v]
		if p1[1] == exclude_pos[1] and p2[0] == exclude_pos[0]:
			return [v + h]
		return[v + h, h + v]

for k1 in keys:
	p1 = find_pos(keypad, k1)
	keypad_distances[k1] = dict()
	for k2 in keys:
		p2 = find_pos(keypad, k2)
		keypad_distances[k1][k2] = calc_moves(p1, p2, [0, 3])
		printD(f"{k1} => {k2} : {keypad_distances[k1][k2]}")

for k1 in arrows:
	p1 = find_pos(keypad_arrows, k1)
	keypad_arrow_distances[k1] = dict()
	for k2 in arrows:
		p2 = find_pos(keypad_arrows, k2)
		keypad_arrow_distances[k1][k2] = calc_moves(p1, p2, [0, 0])
		printD(f"{k1} => {k2}: {keypad_arrow_distances[k1][k2]}")

def shortest_path(code):
	res = keypad_distances[code[0]][code[1]]
	if len(code) == 2:
		return [r + 'A' for r in res]
	sub_list = shortest_path(code[1:])
	full_result = list()
	for prefix in res:
		for suffix in sub_list:
			full_result.append(prefix + 'A' + suffix)
	return full_result

@cache
def find_orders(buttons):
	res = keypad_arrow_distances[buttons[0]][buttons[1]]
	if len(buttons) == 2:
		return [r + 'A' for r in res]
	sub_list = find_orders(buttons[1:])
	full_list = list()
	for r in res:
		for s in sub_list:
			full_list.append(r + 'A' + s)
	return full_list

@cache
def find_split_order(buttons: str, level: int) -> int:
	ss = buttons.split('A')
	lg = 0
	for s in ss[:-1]:
		t_list = find_orders('A' + s + 'A')
		if level > 0:
			min_lg = -1
			for t in t_list:
				cur_lg = find_split_order(t, level -1)
				if min_lg == -1 or cur_lg < min_lg:
					min_lg = cur_lg
			lg += min_lg
		else:
			min_lg = -1
			for t in t_list:
				if min_lg == -1 or len(t) < min_lg:
					min_lg = len(t)
			lg += min_lg
	return lg

def compute(nb_loops):
	total = 0
	for idx,line in enumerate(lines):
		min_len = -1
		printD(line)
		pathes = shortest_path(['A'] + [x for x in line])
		printD(pathes)
		for p in pathes:
			length = find_split_order(p, nb_loops - 1)
			if min_len == -1 or length < min_len:
				min_len = length
		printD(f"{line}: {min_len} * {int(line.replace('A', ''))}")
		total += min_len * int(line.replace('A', ''))
	return total


print(f"Step 1 total: {compute(2)}")
print(f"Step 2 total: {compute(25)}")
