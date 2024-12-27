#!/usr/bin/python3
from starutils import startTest, printD, hasParam, getParam

lines = startTest()
total = 0

map = list()
start = list()
end = list()

dir = [1, 0]

for idx,line in enumerate(lines):
	if "S" in line:
		start = [line.find("S"), idx]
		line = line.replace("S", ".")
	if "E" in line:
		end = [line.find("E"), idx]
		line = line.replace("E", ".")
	map.append([x for x in line])

for l in map:
	print("".join(l))
print(f"Start: {start}, end: {end}")

scores = [[[-1, -1, -1, -1] for _ in range(len(map[0]))] for _ in range(len(map))]

def move(p, d):
	return [p[0] + d[0], p[1] + d[1]]

def calc_possible(n, score, cur_d, old_seq):
	res = list()
	for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
		next_score = score
		if d[0] == - cur_d[0] and d[1] == - cur_d[1]:
			continue
		if d != cur_d:
			next_score += 1000
		res.append([n, d, next_score, old_seq[:] + [n]])
	return res


next_pos = calc_possible(start, 0, [1, 0], [])
scores[start[1]][start[0]] = [0, 0, 0, 0]
min_full_path = -1

def dir2idx(d):
	return int((d[0] + 1) /2) + int((d[1] + 1) / 2) + 2

while next_pos:
	pos = next_pos.pop()
	if min_full_path != -1 and pos[2] > min_full_path:
		continue
	n = move(pos[0], pos[1])
	if map[n[1]][n[0]] == '#':
		#print("Wall")
		continue
	if map[n[1]][n[0]] == '.':

		dir_idx = dir2idx(pos[1])
		if scores[n[1]][n[0]][dir_idx] == -1 or pos[2] + 1 < scores[n[1]][n[0]][dir_idx]:
			scores[n[1]][n[0]][dir_idx] = pos[2] + 1
			next_pos.extend(calc_possible(n, pos[2] + 1, pos[1], []))
			next_pos.sort(key=lambda x: x[2])
			if n == end:
				min_full_path = pos[2] + 1
				#print(f"Append lg:{len(pos[3])+1} [{n}, {d}, {next_score}, {pos[3][:] + [n]}]")
				#print(f"Append lg:{len(pos[3])+1} [{n}, {pos[1]}, {pos[2] + 1}]")

print(f"Best end score {scores[end[1]][end[0]]}")

next_pos = [[start]]
tiles = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]

def count_corners(l):
	count = 0
	dir = [1, 0]
	last = l[0]
	for idx, i in enumerate(l):
		if idx > 0:
			new_dir = [i[0] - last[0], i[1] - last[1]]
			if new_dir != dir:
				count += 1
				dir = new_dir
		last = i
	return count

while next_pos:
	pos = next_pos.pop()
	if len(pos) > (min_full_path%1000):
		continue
	for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
		n = move(pos[-1], d)
		if len(pos)>= 2 and n == pos[-2]:
			continue
		if map[n[1]][n[0]] == '#':
			#print("Wall")
			continue
		if n == end and len(pos) == min_full_path%1000 and count_corners(pos + [n]) == int(min_full_path/1000):
			#print(f"Found {pos + [n]} {count_corners(pos + [n])}")
			for pt in pos + [n]:
				tiles[pt[1]][pt[0]] = 1
		else:
			next_pos.append(pos + [n])

total = 0
for l in tiles:
	print("".join([str(x) for x in l]))
	total += sum(l)
print(f"Step 1 total: {total}")
