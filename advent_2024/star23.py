#!/usr/bin/python3
from starutils import startTest, printD, hasParam

lines = startTest()
total = 0

conns = dict()

for line in lines:
	s = line.split("-")
	if s[0] not in conns:
		conns[s[0]] = list()
	conns[s[0]].append(s[1])
	if s[1] not in conns:
		conns[s[1]] = list()
	conns[s[1]].append(s[0])

for s in conns:
	conns[s].sort()

max_conn = 0
groups = dict()
k = list(conns.keys())
k.sort()
for c in k:
	for idx, l in enumerate(conns[c]):
		if idx == len(conns[c]) - 1:
			continue
		for m in conns[c][idx + 1:]:
			if m in conns[l]:
				g = [c, l, m]
				g.sort()
				groups[tuple(g)] = 1
	printD(f"{c} => {conns[c]}")
	if len(conns[c]) > max_conn:
		max_conn = len(conns[c])

printD(f"Max conn: {max_conn}")

printD("\nGroups:")
k = list(groups.keys())
k.sort()
for idx, c in enumerate(k):
	printD(f"{idx}) {','.join(c)}")

printD("\n with T:")
for idx, c in enumerate(k):
	valid = False
	for t in c:
		if t.startswith("t"):
			valid = True
	if valid:
		total += 1
		printD(f"{total}) {','.join(c)}")

print(f"Step 1 total: {total}")


source = dict()
for k in conns:
	source[tuple([k])] = conns[k]

def merge(lst1, lst2):
	result = list()
	for i in lst1:
		if i in lst2:
			result.append(i)
	return result

longuest_path = []
for i in range(max_conn):
	groups = dict()
	k = list(source.keys())
	k.sort()
	for c in k:
		for l in source[c]:
			m = merge(source[c], conns[l])
			if m:
				lst = list(c) + [l]
				lst.sort()
				groups[tuple(lst)] = m
				if len(m) == 1:
					longuest_path = lst + m

	printD(f"\nGroups lg {i + 2}:")
	k = list(groups.keys())
	k.sort()
	if hasParam("-d"):
		for idx, c in enumerate(k):
			printD(f"{idx}) {','.join(c)} => ({len(groups[c])}) {groups[c]}")
	source = groups
longuest_path.sort()
print(f"Step 2 longuest path: {','.join(longuest_path)} (len: {len(longuest_path)})")
