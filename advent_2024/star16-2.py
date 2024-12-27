#!/usr/bin/python3
from starutils import startTest
import time

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

def move(p, d):
	return [p[0] + d[0], p[1] + d[1]]

def invert_dir(d):
	return [-d[0], -d[1]]

def move_back(p, d):
	return move(p, invert_dir(d))

def calc_score(move, turn):
	return turn * 1000 + move

next_pos = [[start, 0, 0,[1, 0], [start]]]


min_turn = [[1000 for _ in range(len(map[0]))] for _ in range(len(map))]

tiles = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]
tiles[end[1]][end[0]] = 1

start_time = time.time()
next_print_time = start_time + 10
while next_pos:
	current_time = time.time()
	if current_time >= next_print_time:
		print(f"{int(current_time - start_time)}) Processing... len: {len(next_pos)} min_len: {next_pos[0][1]}")
		next_print_time += 10

	next_pos.sort(key=lambda x: x[1], reverse=True)
	pos = next_pos.pop(0)
	if pos[1] > 460 or pos[2] > 102:
		continue
	for d in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
		if d == invert_dir(pos[3]):
			continue
		n = move(pos[0], d)
		if map[n[1]][n[0]] == '#':
			#print("Wall")
			continue

		next_move = pos[1] + 1
		next_turn = pos[2]
		if pos[3] != d:
			next_turn += 1

		if next_turn > min_turn[n[1]][n[0]] + 1:
			continue
		if next_turn < min_turn[n[1]][n[0]]:
			min_turn[n[1]][n[0]] = next_turn
		if n not in pos[4]:
			next_pos.append([n, next_move, next_turn, d, pos[4] + [n]])

		if n == end:
			print(f"Found end:{pos} {n} {d}")
			for p in pos[4]:
				tiles[p[1]][p[0]] = 1



total = 0
for y, l in enumerate(tiles):
	res = ["O" if val==1 else map[y][x] for x,val in enumerate(l)]
	print("".join(res))
	total += sum(l)
print(f"Step 2 total: {total}")
