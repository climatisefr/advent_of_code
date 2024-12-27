#!/usr/bin/python3
from starutils import startTest, printD, toMap, getAt, dir4, move

lines = startTest()
total = 0
[map, sz] = toMap(lines)
heads = list()

for idx, line in enumerate(lines):
	h = [[x, idx] for x,v in enumerate(line) if v == "0"]
	heads.extend(h)
printD(f"Heads: {heads}")

def find_next(pos):
	next_pos = list()
	cur_val = int(getAt(map, pos, sz))
	for dir in dir4:
		n = move(pos, dir)
		n_val = getAt(map, n, sz)
		if not n_val:
			continue
		if cur_val + 1 == int(n_val):
			next_pos.append(n)
	printD(f"p {pos}:{cur_val} => {next_pos}")
	return next_pos


def find_path(src, positions):
	ret_val = dict()
	for p in positions:
		printD(f"pos {p}")
		if getAt(map, p, sz) == "9":
			printD(f"Reach 9 in {p}")
			ident = str(src) + " => " + str(p)
			ret_val[ident] = ret_val.get(ident, 0) + 1
		else:
			n = find_next(p)
			ret = find_path(src, n)
			for r,v in ret.items():
				ret_val[r] = ret_val.get(r, 0) + v
	printD(f"ret_val {ret_val}")
	return ret_val

total2 = 0
for src in heads:
	f = find_path(src, [src])
	sub_total = sum([f[x] for x in f])
	printD(f"{src} => {len(f)} / {sub_total}")
	total += len(f)
	total2 += sub_total

print(f"Step 1 Total: {total}")
print(f"Step 2 Total: {total2}")