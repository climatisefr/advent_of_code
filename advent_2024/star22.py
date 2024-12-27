#!/usr/bin/python3
from starutils import startTest, printD

lines = startTest()
total = 0
init_values = list()

for line in lines:
	init_values.append(int(line))

def calc_next(secret):
	secret = secret ^ (secret << 6)
	secret = secret % 16777216
	secret = secret ^ (secret >> 5)
	secret = secret % 16777216
	secret = secret ^ (secret * 2048)
	secret = secret % 16777216
	return secret

full_gain = dict()
for s in init_values:
	s_init = s
	prev_s = None
	last_deltas = list()
	prev_s = s
	seq_store = dict()
	for i in range(2000):
		s = calc_next(s)
		if prev_s:
			delta = (s%10) - (prev_s%10)
			last_deltas.append(delta)
			if len(last_deltas) > 4:
				last_deltas.pop(0)
			if len(last_deltas) == 4:
				tt = tuple(last_deltas)
				if tt not in seq_store:
					seq_store[tt] = s%10
		printD(f"{prev_s} => {s} p: {s%10} {last_deltas}")
		prev_s = s
	total += s
	for item in seq_store:
		full_gain[item] = full_gain.get(item, 0) + seq_store[item]

max = 0
for i in full_gain:
	printD(f"{i} => {full_gain[i]}")
	if full_gain[i] > max:
		max = full_gain[i]
print(f"Step 1 total: {total}")
print(f"Step 2 max:   {max}")
